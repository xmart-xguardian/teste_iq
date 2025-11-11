from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os
import sys
from pathlib import Path

def resource_path(relative_path):
    # Resolve o caminho para o arquivo, seja em execução normal ou via PyInstaller
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

class UserManagementBot:

    def __init__(self):
        # Configuração inicial do Chrome e WebDriverWait
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--start-maximized')
        self.driver = Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, selector: str, by: object = By.XPATH):
        # Método auxiliar para encontrar elementos
        return self.driver.find_element(by, selector)

    ##########################################
    #               INÍCIO LOGIN             #
    ##########################################
    def login(self):
        # Acessa a página de login
        self.driver.get('http://localhost:5173/')

        #   Preenche os campos de email e senha        
        email_input = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//input[@type="email"]')
        ))
        email_input.send_keys('adriano.angioletto@xmartsolutions.com.br')
        time.sleep(5)

        # Preenche o campo de senha
        password_input = self.find_element('//input[@type="password"]')
        password_input.send_keys('Hotmail.1234@')
        time.sleep(1)

        # Clica no botão de login
        login_button = self.find_element('//button')
        login_button.click()
        time.sleep(5)

    ##########################################
    #           INÍCIO CRIAÇÃO DE USUÁRIO    #
    ##########################################
    def create_test_user(self):

        # Acessa a página de usuários
        users_nav_button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'div.usuariosNavButton[title="Usuários"]')
        ))
        users_nav_button.click()
        time.sleep(5)

        # Clica no botão de adicionar usuário
        add_user_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Adicionar Usuário')]")
        ))
        add_user_button.click()
        time.sleep(1)

        # Preenche os campos de nome, email, senha e cargo
        name_input = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Digite o nome completo']")
        ))
        name_input.send_keys('Ramon testador')
        time.sleep(1)
        
        # Preenche o campo de email
        email_input = self.find_element("//input[@placeholder='exemplo@empresa.com']")
        email_input.send_keys('ramon_testadoor@xmartsolutions.com.br')
        time.sleep(1)

        # Preenche o campo de senha
        password_input = self.find_element("//input[@placeholder='Digite a senha']")
        password_input.send_keys('Hotmail.1dad45@@')
        time.sleep(1)

        # Seleciona o cargo do usuário
        role_select = self.find_element('cargo_id', by=By.ID)
        Select(role_select).select_by_visible_text('Analista de Cyber')
        time.sleep(3)

        # Clica no botão de criar usuário
        create_user_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Criar']"))
        )
        create_user_button.click()
        time.sleep(7)

    ##########################################
    #           INÍCIO CRIAÇÃO DE EQUIPE     #
    ##########################################
    def create_team(self):
        # Acessa a página de equipes
        team_nav_button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'div.equipesNavButton[title="Equipes"]')
        ))
        team_nav_button.click()
        time.sleep(5)

        # Clica no botão de adicionar equipe
        add_team_button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button.createTeamButton')
        ))
        add_team_button.click()
        time.sleep(1)

        # Preenche o nome da equipe
        team_name_input = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@name='name']")
        ))
        team_name_input.send_keys('RamonTestador')
        time.sleep(1)

        # Seleciona o participante da equipe
        participant_select = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//select[@name='users']")
        ))
        Select(participant_select).select_by_visible_text("ramon_testadoor@xmartsolutions.com.br")
        time.sleep(1)

        # Clica no botão de criar equipe
        create_team_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Criar']"))
        )
        create_team_button.click()
        time.sleep(5)

    ##########################################
    #        INÍCIO ADIÇÃO DE APLICAÇÃO      #
    ##########################################
    def add_application(self):
        
        # Acessa a página de aplicações
        app_nav_button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'div.aplicacoesNavButton[title="Aplicações"]')
        ))
        
        app_nav_button.click()
        time.sleep(3)

        # Clica no botão de adicionar aplicação
        add_app_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Adicionar Aplicação')]")
        ))
        add_app_button.click()
        time.sleep(1)

        # Preenche o nome da aplicação
        app_name_input = self.wait.until(EC.presence_of_element_located(
             (By.NAME, "app_name")
        ))
        app_name_input.send_keys('AppRamonTestador')
        time.sleep(1)

        # Preenche a descrição da aplicação
        app_description_input = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@name='description']")
        ))
        app_description_input.click()
        app_description_input.send_keys('Descricaoappteste')
        time.sleep(1)

        # Seleciona a equipe
        team_select = self.wait.until(EC.visibility_of_element_located((By.NAME, "team_id")))
        Select(team_select).select_by_visible_text('RamonTestador')
        time.sleep(1)

        # Seleciona o tipo de linguagem
        try:
            select_language = self.wait.until(EC.element_to_be_clickable((By.NAME, "languages")))
            Select(select_language).select_by_visible_text("Python")
            time.sleep(1)
        except TimeoutException:
            print("❌ Falha ao selecionar a linguagem.")
            self.driver.save_screenshot("erro_dropdown_languages.png")
            raise

        # Clica no botão de criar aplicação
        create_app_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Criar']"))
        )
        create_app_button.click()
        time.sleep(5)

    ##########################################
    #            INICIO SCANNER              #
    ##########################################

    def start_scanner_SCA_SAST(self):
        
        
        if getattr(self, "sast_sca_calls", 0) >= 3:
            return
        
        
        if not hasattr(self, "sast_sca"):
            self.sast_sca = 1
        
     
        if self.sast_sca == 1:

            # Acessa a aplicação
            app_row = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//td[normalize-space()='AppRamonTestador']")
            ))
            app_row.click()
            time.sleep(5)

            # Acessa a aba de Scans
            scans_tab = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[text()='Scans' and contains(@class, 'cursor-pointer')]")
            ))
            scans_tab.click()      
            time.sleep(1)
     
            # Agora clica no botão "Adicionar Scan"
            start_scan_button = self.wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//button[.//text()[normalize-space()='Adicionar Scan'] and not(@disabled)]"
            )))
            
            start_scan_button.click()
            time.sleep(1)
            
        else:

            # Agora clica no botão "Adicionar Scan"
            start_scan_button = self.wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//button[.//text()[normalize-space()='Adicionar Scan'] and not(@disabled)]"
            )))
            
            start_scan_button.click()
            time.sleep(1)
            
            
            

        # Marca o checkbox de SAST
        sast_checkbox = self.wait.until(EC.element_to_be_clickable((By.NAME, "checkbox_sast")))
        
        if not sast_checkbox.is_selected():
            sast_checkbox.click()
            
            
        time.sleep(1)
        
        if self.sast_sca == 1:

            # Marca o checkbox de SCA (caso deseje garantir que está marcado)
            sca_checkbox = self.wait.until(EC.element_to_be_clickable(
                (By.NAME, "checkbox_sca")
            ))

      
            if not sca_checkbox.is_selected():
                sca_checkbox.click()
            time.sleep(1)

        # Preenche o nome do scan
        scan_name_input = self.wait.until(EC.element_to_be_clickable(
            (By.NAME, "scan_name")
        ))
        scan_name_input.clear() 
        
        if self.sast_sca == 1:
            scan_name_input.send_keys("MeuScanAutomatizado")
            time.sleep(1)
        else:
            scan_name_input.send_keys("MeuScanAutomatizado2")
            time.sleep(1)
            
        
        
        # AQUI PRECISO PEGAR EXATAMENTE O CAMINHO DO DESKTOP DO WINDOWS E DEIXAR O USUARIO DINAMICO ENTÃO SÓ INTERESSA \Desktop\scans e dentro de scans, tem o zip
        # Obtém o caminho absoluto para o arquivo ZIP na pasta 'resources'
        
        desktop_path = Path.home() / "Desktop" / "scans"
        
        # Caminho completo para o arquivo zip dentro da pasta scans
        zip_path = desktop_path / "WebGoat.zip"

        # Espera até o input aparecer (mesmo que esteja oculto)
        file_input = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[type='file']")
        ))

        # Envia o caminho do arquivo ZIP
        file_input.send_keys(str(zip_path))
        
        time.sleep(3)

        # Espera o botão "Enviar" aparecer e estar clicável
        submit_button = self.wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//button[@type='submit' and normalize-space()='Enviar']"
        )))
        
        submit_button.click()
        
        
        time.sleep(60)
        
        
        self.sast_sca_calls = getattr(self, "sast_sca_calls", 0) + 1

        if self.sast_sca == 1:
            self.sast_sca = 0
            self.start_scanner_SCA_SAST()

             
            

    ##########################################
    #          FIM SCANNER SCA SAST         #
    ########################################## 

    ###########################################
    #          INICIO SCANNER DAST            #
    ###########################################

    def start_scanner_DAST(self):

        # Clica no botão "Adicionar Scan"
        start_scan_button = self.wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//button[contains(., 'Adicionar Scan')]"
        )))
        start_scan_button.click()
        time.sleep(1)

        # Marca o checkbox de DAST (se ainda não estiver marcado)
        dast_checkbox = self.wait.until(EC.presence_of_element_located(
            (By.NAME, "checkbox_dast")
        ))
        if not dast_checkbox.is_selected():
            dast_checkbox.click()
        time.sleep(1)

        # Preenche o campo "scan_version_dast" com o nome do scan
        scan_version_input = self.wait.until(EC.element_to_be_clickable(
            (By.NAME, "scan_version_dast")
        ))
        scan_version_input.send_keys("MeuScanAutomatizadoDAST")
        time.sleep(1)

        # Preenche o campo "scan_url_dast" com a URL da aplicação
        site_url_input = self.wait.until(EC.element_to_be_clickable(
            (By.NAME, "site_url")
        ))
        site_url_input.send_keys("https://bancocn.com")
        time.sleep(1)

        # Verifica se o campo de autenticação está ativo e desativa, se necessário
        auth_checkbox = self.wait.until(EC.presence_of_element_located(
            (By.NAME, "authexist")
        ))

        if auth_checkbox.is_selected():
            auth_checkbox.click()
            time.sleep(1)  # espera pela reação do sistema

        # Espera o botão "Enviar" ficar clicável e clica nele
        submit_button = self.wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//button[@type='submit' and normalize-space()='Enviar']"
        )))
        submit_button.click()
        time.sleep(2)  # tempo maior para o scan começar ou feedback aparecer
                
    ###########################################
    #          FIM SCANNER DAST              #
    ###########################################

    ##########################################
    #          INICIO SCANNER CONTAINER      #
    ##########################################

    def start_scanner_container(self):
        
        # Clica no botão "Adicionar Scan"
        start_scan_button = self.wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//button[contains(., 'Adicionar Scan')]"
        )))
        start_scan_button.click()
        time.sleep(1)

        # Marca o checkbox de Container (se ainda não estiver marcado)
        container_checkbox = self.wait.until(EC.presence_of_element_located(
            (By.NAME, "checkbox_container")
        ))
        if not container_checkbox.is_selected():
            container_checkbox.click()
        
        time.sleep(1)
       
        # Preenche o campo com o nome do scan
        scan_version_input = self.wait.until(EC.element_to_be_clickable(    
            (By.NAME, "scan_name")
        ))
        scan_version_input.send_keys("MeuScanAutomatizadoContainer")
        time.sleep(1)
        
        desktop_path = Path.home() / "Desktop" / "scans"
        
        # Caminho completo para o arquivo tar dentro da pasta scans
        zip_path = desktop_path / "webgoatcont.tar"
        
        # Espera até o input aparecer (mesmo que esteja oculto)
        file_input = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[type='file']")
        ))
        # Envia o caminho do arquivo ZIP
        file_input.send_keys(str(zip_path))
        
        time.sleep(1)

       # Espera o botão "Enviar" aparecer e estar clicável
        submit_button = self.wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//button[@type='submit' and normalize-space()='Enviar']"
        )))
        submit_button.click()

        time.sleep(100)

    ##########################################
    #          FIM SCANNER CONTAINER         #
    ##########################################

    def run(self):
        self.login()
        self.create_test_user()
        self.create_team()
        self.add_application()
        self.start_scanner_SCA_SAST()
        self.start_scanner_DAST()
        self.start_scanner_container()

        self.driver.quit()
    
