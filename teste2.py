from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import time



class StartTests:
    
    senha = 545787659
    
    def __init__(self):
        
        
        self.chrome_opcao = ChromeOptions()
        
        self.chrome_opcao.add_argument('--start-maxdimized') 
        
        
        self.drive = Chrome(self.chrome_opcao) 
        

    def EncontraElementos(self, valor: str, Element: object = By.XPATH,) -> object:
                                                     
            elemento = self.drive.find_element(Element, valor)
                
            
            return elemento
    
    
    
    def StartRobo(self):
        
        time.sleep(2)
        
        self.drive.get('http://localhost:5173/')
        
        time.sleep(2)
        

        element = self.EncontraElementos('/html/body/div[1]/div[1]/div[1]/div/div[2]/form/div/div[1]/div/label/div/input') # CAMPO EMAIL < 
        
        element.click()
        
        element.send_keys('joaovnt@icloud.com')
        
        time.sleep(2)
        
        element_login_2 = self.EncontraElementos('/html/body/div[1]/div[1]/div[1]/div/div[2]/form/div/div[2]/div/label/div/input') # CAMPO SENHA 
        
        element_login_2.click()
        
        time.sleep(2) 
        
        element_login_2.send_keys('Joaodedados@123')
        
        time.sleep(2) 
        
        button_acesss = self.EncontraElementos('/html/body/div[1]/div[1]/div[1]/div/div[2]/form/div/div[3]/button')
        
        button_acesss.click()

        
        time.sleep(10)
        
        
    


cls = StartTests(
)

cls.StartRobo()