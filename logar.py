#Importando bibliotecas a serem utilizadas
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
email = input("Qual é seu e-mail? ")
senha = input("Qual é sua senha de email? ")
#Abrindo o driver do chrome para abrir o navegador
driver = webdriver.Chrome()

#Abrindo site do Google
driver.get("https://www.google.com")

# Encontrar o elemento de login na página
login_elem = driver.find_element(By.CLASS_NAME,"gb_ia.gb_ja.gb_fe.gb_fd")

# Clicar no botão de login
login_elem.click()

email_elem = driver.find_element(By.CLASS_NAME,"whsOnd.zHQkBf")
email_elem.send_keys(f"{email}")
email_elem.send_keys(Keys.RETURN)

#Entrando na tela de senha do google
sleep(10)
pass_elemt = driver.find_element(By.CLASS_NAME,"whsOnd.zHQkBf")
pass_elemt.send_keys(f"{senha}")
pass_elemt.send_keys(Keys.RETURN)
#Houve a nescessidade do sleep() para esperar a tela de carregamento do google
sleep(10)

# Encontrar os campos de email e senha na página

password_elem = driver.find_element_by_name("password")

# Preencher os campos com as credenciais da sua conta
email_elem.send_keys("granatellisanches@gmail.com")
password_elem.send_keys("Principe13*")

# Enviar o formulário de login
password_elem.send_keys(Keys.RETURN)