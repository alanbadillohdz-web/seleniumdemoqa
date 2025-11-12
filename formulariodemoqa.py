from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configura opciones seguras
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Inicializa el driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    # Abre demoqa.com
    driver.get("https://demoqa.com/")

    # Espera y fuerza el clic en "Forms" usando JavaScript
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h5[text()='Forms']"))
    )
    forms_card = driver.find_element(By.XPATH, "//h5[text()='Forms']")
    driver.execute_script("arguments[0].scrollIntoView(true);", forms_card)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", forms_card)

    # Espera y fuerza el clic en "Practice Form"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Practice Form']"))
    )
    practice_form = driver.find_element(By.XPATH, "//span[text()='Practice Form']")
    driver.execute_script("arguments[0].scrollIntoView(true);", practice_form)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", practice_form)

    # Espera a que cargue el formulario
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "firstName"))
    )

    # Llena los campos
    driver.find_element(By.ID, "firstName").clear()
    driver.find_element(By.ID, "firstName").send_keys("Alan")

    driver.find_element(By.ID, "lastName").clear()
    driver.find_element(By.ID, "lastName").send_keys("Francisco")

    driver.find_element(By.ID, "userEmail").clear()
    driver.find_element(By.ID, "userEmail").send_keys("alan@example.com")

    driver.find_element(By.ID, "userNumber").clear()
    driver.find_element(By.ID, "userNumber").send_keys("5551234567")

    # Clic en género usando JavaScript
    gender_label = driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
    driver.execute_script("arguments[0].click();", gender_label)

    # Enviar el formulario
    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].click();", submit_button)

    print("Formulario enviado correctamente desde la página principal.")

except Exception as e:
    print(f"Error: {e}")
   print("Nueva ejecución para validar captura")

finally:
    driver.quit()