from PySide6.QtWidgets import QWidget, QMessageBox, QLabel, QLineEdit, QPushButton
from PySide6.QtGui import QCursor
from PySide6.QtCore import Qt, QTimer,  QThread, Signal
import ui_after_login
import requests
import get_token
from robo_testes import UserManagementBot
import sys
from aws import AwsDb


class RoboThread(QThread):
    
    #thread separada para evitar que interface fique na tread principal.
    
    finished = Signal()
    error = Signal(str)

    def run(self):
        try:
            bot = UserManagementBot()
            bot.run()
            self.finished.emit()
        except Exception as e:
            self.error.emit(str(e))


class TelaPrincipal(QWidget):
    
    
    
    
    def __init__(self):
        super().__init__()
        self.ui = ui_after_login.Ui_Form()
        self.ui.setupUi(self)

        self.orgs_data = []

   
        self.label_scans = QLabel("Scans disponíveis:", self.ui.widget_2)
        self.label_scans.setGeometry(10, 140, 120, 24) 
        self.label_scans.setStyleSheet("color: black; font-size: 13px; background: transparent;")

        self.input_scans = QLineEdit(self.ui.widget_2)
        self.input_scans.setGeometry(135, 140, 60, 24)
        self.input_scans.setStyleSheet("background-color: rgb(77, 39, 122); color: white;")
        self.input_scans.setPlaceholderText("0")

        self.btn_alterar = QPushButton("Alterar", self.ui.widget_2)
        self.btn_alterar.setGeometry(200, 140, 70, 24)
        self.btn_alterar.setStyleSheet("background-color: rgb(77, 39, 122); color: white; border-radius: 5px;")
        self.btn_alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar.clicked.connect(self.alterar_valor_scans)

        # Esconde por padrão
        self.label_scans.hide()
        self.input_scans.hide()
        self.btn_alterar.hide()
        
        # Eventos
        self.ui.pushButton.clicked.connect(self.buscar_api)
        
        self.ui.pushButton_2.clicked.connect(self.ligar_banco)  
        
        self.ui.pushButton_4.clicked.connect(self.StartRobo)
        
        self.ui.pushButton_3.clicked.connect(sys.exit)
        self.ui.comboBox.currentIndexChanged.connect(self.exibir_scans_disponiveis)
        
        
    

    def buscar_api(self):
        url = "https://reporter.xguardianplatform.io/get_org_internal"
        print("Token atual:", get_token.token)

        try:
            headers = {
                "Authorization": f"Bearer {get_token.token}",
                "Content-Type": "application/json"
            }
            resposta = requests.get(url, headers=headers)

            if resposta.status_code == 200:
                resultado = resposta.json()

                if isinstance(resultado, dict) and "organizations" in resultado:
                    orgs = resultado["organizations"]
                elif isinstance(resultado, list):
                    orgs = resultado
                else:
                    orgs = []

                self.orgs_data = orgs
                self.ui.comboBox.clear()

                for org in orgs:
                    nome = org.get("name", "Nome desconhecido")
                    self.ui.comboBox.addItem(nome)

                if orgs:
                    self.ui.comboBox.setCurrentIndex(0)
                    self.exibir_scans_disponiveis()

                QMessageBox.information(self, "Busca Completa", "Organizações carregadas com sucesso!")
            else:
                QMessageBox.warning(self, "Erro", f"Status: {resposta.status_code}\n{resposta.text}")
        except Exception as e:
            QMessageBox.critical(self, "Erro de conexão", str(e))
    
    def StartRobo(self):
        QMessageBox.information(self, "Ligando Robô", "Não se esqueça de ativar o ambiente do front local !! , Abrindo o Google Chrome aguarde... ")
        self.robo_thread = RoboThread()
        self.robo_thread.finished.connect(lambda: QMessageBox.information(self, "Robô", "Robô terminou!"))
        self.robo_thread.error.connect(lambda msg: QMessageBox.critical(self, "Erro no Robô", msg))
        self.robo_thread.start()
    
    def ligar_banco(self):
        
        awsdb = AwsDb()
        
        resultado = awsdb.alternar_estado()
        
        self.ui.pushButton_2.setText(resultado)
        
        QMessageBox.information(self, "AWS RDS", f"{resultado} banco '{awsdb.db_instance_id}'!")

        self.ui.pushButton_2.setEnabled(False)
        
        self.ui.pushButton_2.setText("Aguarde 3:30...")


        QTimer.singleShot(210000, self.reativar_botao)

    def reativar_botao(self):
        self.ui.pushButton_2.setEnabled(True)
        self.ui.pushButton_2.setText("Ligar/Desligar Banco")
            
        
        

    def exibir_scans_disponiveis(self):
        index = self.ui.comboBox.currentIndex()
        if 0 <= index < len(self.orgs_data):
            org = self.orgs_data[index]
            scans = org.get("scansAvailable", "")

            
            self.label_scans.show()
            self.input_scans.show()
            self.btn_alterar.show()
            self.input_scans.setText(str(scans))
        else:
           
            self.label_scans.hide()
            self.input_scans.hide()
            self.btn_alterar.hide()

    def alterar_valor_scans(self):
        index = self.ui.comboBox.currentIndex()
        if 0 <= index < len(self.orgs_data):
            org = self.orgs_data[index]
            nome_org = org.get("name", "Organização desconhecida")
            novo_valor = self.input_scans.text()

            if novo_valor.isdigit():
                novo_valor_int = int(novo_valor)
                org["scansAvailable"] = novo_valor_int 

                # Dados para enviar
                payload = {
                    "org_name": nome_org,
                    "xscans_alt": novo_valor_int
                }

                url_alterar = "https://reporter.xguardianplatform.io/post_org_internal"  

                headers = {
                    "Authorization": f"Bearer {get_token.token}",
                    "Content-Type": "application/json"
                }

                try:
                    resposta = requests.post(url_alterar, json=payload, headers=headers)
                    
                    if resposta.status_code in (200, 204):
                        QMessageBox.information(self, "Sucesso", f"Alteração enviada para '{nome_org}' com valor {novo_valor_int}.")
                    else:
                        QMessageBox.warning(self, "Erro", f"Falha na alteração.\nStatus: {resposta.status_code}\n{resposta.text}")
                except Exception as e:
                    QMessageBox.critical(self, "Erro de conexão", str(e))

            else:
                QMessageBox.warning(self, "Erro", "Digite um número válido.")


