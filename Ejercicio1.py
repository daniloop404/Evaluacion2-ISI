from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# Inicializar el driver de Selenium (en este caso, Chrome)
driver = webdriver.Chrome()

# Ajustar el tamaño de la ventana del navegador
driver.set_window_size(1600, 900)

# Abrir la página web
driver.get("https://www.demoblaze.com/index.html")
time.sleep(3)  # Esperar 3 segundos para que la página cargue

# Esperar a que el botón de registro esté disponible y hacer clic en él
wait = WebDriverWait(driver, 10)
sign_up_button = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='signin2']")))
sign_up_button.click()
time.sleep(3)  # Esperar 3 segundos después de hacer clic

# Ingresar el nombre de usuario y contraseña en los campos correspondientes
username_field = driver.find_element(By.XPATH, "//*[@id='sign-username']")
username_field.send_keys("danielsam21ITSQMET")
password_field = driver.find_element(By.XPATH, "//*[@id='sign-password']")
password_field.send_keys("12345")

# Hacer clic en el botón de registro
sign_up_button = driver.find_element(By.XPATH, "//*[@id='signInModal']/div/div/div[3]/button[2]")
sign_up_button.click()
time.sleep(3)  # Esperar 3 segundos después de hacer clic

# Aceptar la alerta
alert = wait.until(EC.alert_is_present())
alert.accept()
time.sleep(3)  # Esperar 3 segundos después de aceptar la alerta

# Hacer clic en el botón de inicio de sesión
login_button = driver.find_element(By.XPATH, "//*[@id='login2']")
login_button.click()
time.sleep(3)  # Esperar 3 segundos después de hacer clic

# Ingresar el nombre de usuario y contraseña en los campos correspondientes
username_field = driver.find_element(By.XPATH, "//*[@id='loginusername']")
username_field.send_keys("danielsam21ITSQMET")
password_field = driver.find_element(By.XPATH, "//*[@id='loginpassword']")
password_field.send_keys("12345")

# Hacer clic en el botón de inicio de sesión
login_button = driver.find_element(By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]")
login_button.click()
time.sleep(3)  # Esperar 3 segundos después de hacer clic

# Seleccionar un producto de forma aleatoria y hacer clic en él
product_divs = driver.find_elements(By.XPATH, "//*[@id='tbodyid']/div//a")
random_product_index = random.randint(0, len(product_divs) - 1)
selected_product = product_divs[random_product_index]
selected_product.click()
time.sleep(3)  # Esperar a que la página del producto cargue

# Ahora en la página de detalles del producto, buscar y hacer clic en el botón "Add to cart"
add_to_cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='tbodyid']/div[2]/div/a"))
)
add_to_cart_button.click()
time.sleep(3)  # Esperar 3 segundos después de hacer clic

# Aceptar la alerta
alert = wait.until(EC.alert_is_present())
alert.accept()
time.sleep(3)  # Esperar 3 segundos después de aceptar la alerta

# Ir a la página de inicio
home_button = driver.find_element(By.XPATH, "//*[@id='navbarExample']/ul/li[1]/a")
home_button.click()
time.sleep(3)  # Esperar 3 segundos después de hacer clic

# Seleccionar un producto de forma aleatoria y hacer clic en él
product_divs = driver.find_elements(By.XPATH, "//*[@id='tbodyid']/div//a")
random_product_index = random.randint(0, len(product_divs) - 1)
selected_product = product_divs[random_product_index]
selected_product.click()
time.sleep(3)  # Esperar a que la página del producto cargue

# Ahora en la página de detalles del producto, buscar y hacer clic en el botón "Add to cart"
add_to_cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='tbodyid']/div[2]/div/a"))
)
add_to_cart_button.click()
time.sleep(3)  # Esperar 3 segundos después de hacer clic

# Aceptar la alerta
alert = wait.until(EC.alert_is_present())
alert.accept()
time.sleep(3)  # Esperar 3 segundos después de aceptar la alerta

# Ir al carrito de compras
cart_button = driver.find_element(By.XPATH, "//*[@id='cartur']")
cart_button.click()
time.sleep(3)  # Esperar 3 segundos después de hacer clic

# Hacer clic en el botón de realizar pedido
place_order_button = driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div/div[2]/button")
place_order_button.click()
time.sleep(3)  # Esperar 3 segundos después de hacer clic

# Ingresar los datos del pedido
name_field = driver.find_element(By.XPATH, "//*[@id='name']")
name_field.send_keys("Daniel Sampedro")
country_field = driver.find_element(By.XPATH, "//*[@id='country']")
country_field.send_keys("Ecuador")
city_field = driver.find_element(By.XPATH, "//*[@id='city']")
city_field.send_keys("Quito")
credit_card_field = driver.find_element(By.XPATH, "//*[@id='card']")
credit_card_field.send_keys("1234567890123456")
month_field = driver.find_element(By.XPATH, "//*[@id='month']")
month_field.send_keys("Agosto")
year_field = driver.find_element(By.XPATH, "//*[@id='year']")
year_field.send_keys("2024")

# Hacer clic en el botón de compra
purchase_button = driver.find_element(By.XPATH, "//*[@id='orderModal']/div/div/div[3]/button[2]")
purchase_button.click()
time.sleep(3)  # Esperar 3 segundos después de hacer clic

# Aceptar el mensaje de confirmación
confirm_button = driver.find_element(By.XPATH, "/html/body/div[10]/div[7]/div/button")
confirm_button.click()
time.sleep(3)  # Esperar 3 segundos después de hacer clic

# Cerrar sesión
logout_button = driver.find_element(By.XPATH, "//*[@id='logout2']")
logout_button.click()
time.sleep(3)  # Esperar 3 segundos después de hacer clic

# Cerrar el navegador
driver.quit()