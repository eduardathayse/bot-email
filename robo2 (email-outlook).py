from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# from selenium.webdriver.common.action_chains import ActionChains # Importar a classe ActionChains responsável pelas manipulações

print("Iniciando o Robô...")
time.sleep(1)

# Atribuição de variáveis
file = open("login.txt", "r")
linhas = file.readlines()
for l in linhas:
    dados = l.split(";")

email = dados[0]
senha = dados[1]
destinatario = dados[2]
assunto = "Robô."
mensagem = "E-mail enviado pelo robo2."

# Atribuindo o driver
# driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chrome")
driver = webdriver.Chrome("C:/chromedriver.exe")
time.sleep(2)

# Acessando o email (outlook)
print("Acessando o Outlook...")
driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1592855715&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3dd4e23bfb-aba5-3203-0e4b-3e9d4b62babd&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015")
time.sleep(3)

# Realizando LOGIN

# Email
print("Realizando login...")
login = driver.find_element_by_id("i0116")
login.clear()
login.send_keys(email)
time.sleep(1)
login.send_keys(Keys.ENTER)
time.sleep(2)

# Senha
password = driver.find_element_by_id("i0118")
password.clear()
password.send_keys(senha)
password.send_keys(Keys.ENTER)
print("Login Realizado!")
time.sleep(10)

# Abrindo a caixa de email
print("Abrindo caixa de Email...")
driver.get("https://outlook.live.com/mail/0/deeplink/compose?version=2020062103.04&popoutv2=1")

time.sleep(3)

# Encontrando o box do destinatário
print("Digitando Email...")
boxDesti = driver.find_element_by_xpath("//input[@aria-label='Para']")
boxDesti.send_keys(destinatario)
time.sleep(0.5)
boxDesti.send_keys(Keys.ENTER)

# Encontrando o box do assunto da mensagem
boxAssunto = driver.find_element_by_id("TextField20")
boxAssunto.send_keys(assunto)
boxAssunto.send_keys(Keys.ENTER)

# Encontrando o box da mensagem
boxMensa = driver.find_element_by_xpath("//div[@role='textbox']") # div é o elemento que o robo vai procurar (<div> </div>), e o role é o atributo que o robo vai procurar dentro da div (<div> role </div>)(ex.: se fosse pelo id seria -> //div[@id='ap'])
boxMensa.send_keys(mensagem)
time.sleep(2)

# Enviando email
print("Enviando Email...")
enviar = driver.find_element_by_xpath("//span[@data-automationid='splitbuttonprimary']")
enviar.click() # para clicar com o botão esquerdo do mouse
time.sleep(2)
print("====== Email Enviado Com Sucesso! ======")

time.sleep(10)
driver.close()