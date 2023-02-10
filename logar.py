
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.google.com")

# Encontrar o elemento de login na página
login_elem = driver.find_element(By.CLASS_NAME,"gb_ia.gb_ja.gb_fe.gb_fd")

# Clicar no botão de login
login_elem.click()

email_elem = driver.find_element(By.CLASS_NAME,"whsOnd.zHQkBf")
email_elem.send_keys("granatellisanches@gmail.com")
email_elem.send_keys(Keys.RETURN)

sleep(10)
pass_elemt = driver.find_element(By.CLASS_NAME,"whsOnd.zHQkBf")
pass_elemt.send_keys("Principe13*")
pass_elemt.send_keys(Keys.RETURN)
sleep(1000)

# Encontrar os campos de email e senha na página

password_elem = driver.find_element_by_name("password")

# Preencher os campos com as credenciais da sua conta
email_elem.send_keys("granatellisanches@gmail.com")
password_elem.send_keys("Principe13*")

# Enviar o formulário de login
password_elem.send_keys(Keys.RETURN)

