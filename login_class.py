import requests
from PySide6.QtWidgets import QMessageBox
import sys

import get_token



class login():
    """
    Classe responsável por realizar o login no sistema.
    """
    def __init__(self, username, password):
        
        self.url = 'https://auth.xguardianplatform.io/login'
        
        self.username = username
        
        self.password = password

    def authenticate(self):
        
        if not self.username.strip() or not self.password.strip():

            QMessageBox.warning(
                None,
                "Login",
                "Preencha o usuário e a senha."
            )
            
           
            return None
            

        payload = {
            "email": self.username,
            "password": self.password,
            "recaptcha_token": "string"
        }

        try:
            response = requests.post(
                self.url,
                json=payload,
            )
            result = response.json()
            
            get_token.token = result['token']
    

            if response.status_code == 200 and "token" in result:
                QMessageBox.information(
                    None,
                    "Login",
                    "Login realizado com sucesso!"
                )
                
                return 1

            elif "detail" in result:
                detail = result["detail"]
                if "Usuário ou senha incorretos" in detail:
                    QMessageBox.warning(
                        None,
                        "Login",
                        "Usuário ou senha incorretos."
                    )
                    
                    return None
                else:
                    QMessageBox.warning(
                        None,
                        "Login",
                        f"Erro: {detail}"
                    )
                    return f"Erro: {detail}"

            else:
                QMessageBox.warning(
                    None,
                    "Login",
                    "Erro desconhecido ao fazer login."
                )
                return "Erro desconhecido ao fazer login."

        except Exception as e:
            QMessageBox.critical(
                None,
                "Login",
                f"Erro de conexão: {str(e)}"
            )
            return 0