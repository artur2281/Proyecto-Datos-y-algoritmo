from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('.\driver\chromedriver')
browser = webdriver.Chrome(options=chromeOptions)
def enviarMensaje():
    
    chatbox = browser.find_element(By.TAG_NAME,'footer')
    chatbox.send_keys('Hola')
    chatbox.send_keys(Keys.ENTER)

def validQR():
    try:
        element = browser.find_element(By.TAG_NAME,'canvas')
    except:
        return False
    return True



def seleccionChat(nombre : str):
    print("buscamos chat")
    try:
        elements = browser.find_element(By.XPATH, "//div[@class='lhggkp7q ln8gz9je rx9719la']//span[@title='" + nombre + "']")
        print("Se encontró el chat")
        elements.click()
    except:
        print("Chat no encontrado")

def botWhatsapp():
    browser.get('https://web.whatsapp.com/')
    time.sleep(5)
    espera = True
    while espera :
        print("Estamos esperando")
        espera = validQR()
        time.sleep(2)
        if espera== False :
            print("QR ingresado")
            break
    time.sleep(5)
    
    numero = 'Neuton'

    chat = seleccionChat(numero)
    
    
    print("fin")


botWhatsapp()
time.sleep(40)