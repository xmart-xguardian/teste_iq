from PySide6.QtWidgets import QApplication, QWidget, QLabel, QMessageBox
from PySide6.QtGui import QPixmap, QIcon, QMovie, QShortcut, QKeySequence
import ui_form
import webbrowser
import sys
import os
from login_class import login  # classe que checa e faz login
from tela_after_login import TelaPrincipal
from aviso_caps_lock import CapsLockWatcher
import time

class Interface():
    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    def show_spinner(self):
        self.ui.label_spinner.setVisible(True)
        self.movie = QMovie(self.resource_path("spinner.gif"))
        self.ui.label_spinner.setMovie(self.movie)
        self.movie.start()

    def hide_spinner(self):
        self.ui.label_spinner.setVisible(False)
        if hasattr(self, "movie"):
            self.movie.stop()

    def do_login(self):
        """Responsável por realizar o login do usuário e chamar próxima página"""
        email = self.ui.lineEdit_3.text()
        senha = self.ui.lineEdit_2.text()
        self.show_spinner()
        login_obj = login(username=email, password=senha)
        resultado = login_obj.authenticate()

        if resultado:
            self.tela_principal = TelaPrincipal()
            self.tela_principal.ui.label.setPixmap(QPixmap(self.resource_path("xguardian_ico.ico")))
            self.tela_principal.ui.label.setScaledContents(True)
            self.tela_principal.setWindowIcon(QIcon(self.resource_path("xguardian_ico.ico")))
            self.tela_principal.setFixedSize(800, 450)
            self.tela_principal.show()
            self.tela_principal.raise_()
            self.tela_principal.activateWindow()
            self.window.close()
        else:
            self.hide_spinner()

    def abre_navegador(self):
        url = "https://shield.xguardianplatform.io/esqueci-minha-senha"
        webbrowser.open(url)

    def set_images(self):
        "responsável por setar as imagens de início do programa"
        self.ui.label.setPixmap(QPixmap(self.resource_path("mulher_ti.jpg")))
        self.ui.label_2.setPixmap(QPixmap(self.resource_path("logo_cabeca.png")))
        self.window.setWindowIcon(QIcon(self.resource_path("xguardian_ico.ico")))
        self.ui.label_spinner.setPixmap(QPixmap(self.resource_path("spinner.gif")))

    def main(self):
        app = QApplication([])

        self.window = QWidget()
        self.window.setFixedSize(800, 450)
        self.ui = ui_form.Ui_XGuardian()
        self.ui.setupUi(self.window)
        self.set_images()

        # Adiciona label de aviso do Caps Lock
        self.label_capslock = QLabel("", self.window)
        self.label_capslock.setGeometry(10, 420, 300, 20)  # Ajuste a posição conforme necessário
        self.label_capslock.setStyleSheet("color: red; font-weight: bold;")
        self.label_capslock.setVisible(False)

        # Instala o filtro de eventos para Caps Lock
        self.capslock_watcher = CapsLockWatcher(self.label_capslock)
        self.window.installEventFilter(self.capslock_watcher)

        # EVENTOS DE CLICK FECHAR ESC, CLICK, E ENTER
        self.ui.pushButton.clicked.connect(self.do_login)
        self.ui.pushButton_2.clicked.connect(self.abre_navegador)
        self.ui.lineEdit_2.returnPressed.connect(self.do_login)
        self.ui.lineEdit_3.returnPressed.connect(self.do_login)

        shortcut = QShortcut(QKeySequence("Escape"), self.window)
        shortcut.activated.connect(self.window.close)
        # FIM DOS EVENTOS DE CLICK ########

        self.window.show()
        app.exec()

if __name__ == "__main__":
    Interface().main()