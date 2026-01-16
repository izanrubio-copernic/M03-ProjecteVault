import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# 1. Configuració de Chrome per a entorns CI/CD (Headless)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Execució sense finestra
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Inicialització del driver amb les opcions
driver = webdriver.Chrome(options=chrome_options)

# Ruta del fitxer login.html
file_path = "file://" + os.path.abspath("login.html")

# 2. Llista de contrasenyes per l'atac de diccionari
passwords = ['1234', 'qwerty', 'admin', 'password123', 'letmein']
usuari_target = "admin"
vulnerabilitat_trobada = False

try:
    for pwd in passwords:
        driver.get(file_path)
        # Localitzar elements
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "loginBtn")

        # Injectar dades
        username_field.send_keys(usuari_target)
        password_field.send_keys(pwd)
        print(f"Provant contrasenya: {pwd}")
        login_button.click()
        # Espera curta per a la resposta del script JS
        time.sleep(1)
        # 3. Comprovar resultat
        resultat = driver.find_element(By.ID, "message").text
        if resultat == "ACCESS_GRANTED":
            print("\n-------------------------")
            print("VULNERABILITAT TROBADA")
            print(f"Contrasenya correcta: {pwd}")
            print("-------------------------")
            # Captura de pantalla d'evidència
            driver.save_screenshot('hacked.png')
            vulnerabilitat_trobada = True
            break
finally:
    driver.quit()

# 4. Sortida estratègica per a la Pipeline
if vulnerabilitat_trobada:
    # Sortim amb error (1) perquè GitHub Actions marqui el test com a FALLIT (vermell)
    sys.exit(1)
else:

    # Si no troba res, la pipeline seguiria en verd
    sys.exit(0)
