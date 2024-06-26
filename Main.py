from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd

# Inicializando webdriver
driver = webdriver.Chrome()

# Inicializando Parametros Globais
df = pd.read_excel('Config.xlsx')
parametros = {}
for index, row in df.iterrows():
    parametro = row['Paramater']
    valor = row['Value']
    parametros[parametro] = valor


def WaitElementByXpath(xpath, timeout):
    try:
        elemento = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return elemento

    except Exception:
        print(f"O elemento com XPath '{xpath}' não foi encontrado após {
              timeout} segundos.")
        return None


def WaitElementByID(id, timeout):
    try:
        elemento = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, id))
        )
        return elemento

    except Exception:
        print(f"O elemento com ID '{id}' não foi encontrado após {
              timeout} segundos.")
        return None


def WaitElementByContainsText(tag, text, timeout):
    try:
        elemento = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, "//"+tag +
                                            "[contains(text(),'"+text+"')]"))
        )
        return elemento

    except Exception:
        print(f"Elemento não encontrado com a tag {tag} e texto: {text}.")
        return None


def findElementByXPATH(xpath):
    return WaitElementByXpath(xpath, parametros['element_timeout'])


def findElementByID(id):
    return WaitElementByID(id, parametros['element_timeout'])


def findElementByContainsText(tag, text):
    return WaitElementByContainsText(tag, text, parametros['element_timeout'])


def initAllApplications():
    # Iniciando navegador
    try:
        print("Inicializando as aplicações.")
        # driver.close()
        driver.get('https://rpachallenge.com/')
        print("Finalizado inicialização das aplicações.")
    except Exception as e:
        print(f"Falha ao inicializar as aplicações. Erro: {e}")


# Main workflow
initAllApplications()

transactionNumber = 1

while transactionNumber <= parametros["max_retry"]:
    try:
        print("Inicializando o processamento.")

        findElementByID("teste").click()
        print("Finalizado o processamento.")
        break
    except Exception:
        print(Exception)
        if transactionNumber <= parametros:
            initAllApplications()

    transactionNumber += 1
