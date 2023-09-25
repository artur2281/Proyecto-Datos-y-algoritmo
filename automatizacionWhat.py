from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

class Automatizacion:
    def __init__(self):
        options = Options()
        options = webdriver.ChromeOptions()
        options.add_argument("--user-data-dir=C:\\Users\\USER\\AppData\\Local\\Google\\Chrome SxS\\User Data")
        options.add_argument("--profile-directory=Default")
        self.driver = webdriver.Chrome(options=options)

    def enviar_imagen(self, ruta_imagen):
        clip_icon = self.driver.find_element(By.CSS_SELECTOR, "span[data-icon='attach-menu-plus']")
        clip_icon.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-icon='attach-menu-plus']")))
        clip_icon2 = self.driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div/div/span/div/ul/div/div[2]/li')
        clip_icon2.click()
        file_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(ruta_imagen)
        send_icon = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span')
        send_icon.click()

    def validar_qr(self):
        try:
            element = self.driver.find_element(By.TAG_NAME, 'canvas')
        except:
            return False
        return True

    def enviar_mensaje(self, numero_telefono, nombre):
        self.driver.get(f"https://web.whatsapp.com/send?phone={numero_telefono}")
        espera = True
        while espera:
            print("Estamos esperando")
            espera = self.validar_qr()
            time.sleep(2)
            if not espera:
                print("QR ingresado")
                break
        time.sleep(1)
        wait = WebDriverWait(self.driver, 150)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'footer')))
        mensaje = f"Felicidades {nombre}, esperamos que tengas un excelente día"
        test = self.driver.find_element(By.TAG_NAME, 'footer')
        message_box = test.find_element(By.TAG_NAME, 'p')
        message_box.click()
        message_box.send_keys(mensaje)
        time.sleep(2)
        message_box.send_keys(Keys.ENTER)
        print(f"Mensaje enviado a {numero_telefono}: {mensaje}")



    def bot_whatsapp(self, numero, ruta_imagen, nombre):
        self.enviar_mensaje(numero, nombre)
        self.enviar_imagen(ruta_imagen)
        
