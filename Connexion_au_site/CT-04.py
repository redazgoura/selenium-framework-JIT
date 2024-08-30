from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep

# renseigner le chemin de votre msedgedriver dans executable_path
service = Service(executable_path=r'C:\edgedriver\msedgedriver.exe')
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options) # Define browser outside the try block

# driver.get("https://www.jumia.ma/")

try:
    driver.maximize_window()

    # Open the browser
    driver.get("https://www.jumia.ma")
    
    # Wait for the element to be clickable
    wait = WebDriverWait(driver, 10)
    button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#pop .cls"))
    )

    # Click the button
    button.click()

    wait = WebDriverWait(driver, 10)
    dropdown_trigger = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='dpdw-login']"))
    )

    # Click the dropdown trigger
    dropdown_trigger.click()


    login_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#dpdw-login-box a.btn._prim"))
    )
    login_button.click()

    emailInput = wait.until(
        EC.visibility_of_element_located((By.ID, "input_identifierValue"))  
    )

    # Fill the email input field
    emailAddress = "redazr1997@gmail.com"  
    emailInput .send_keys(emailAddress)

    continuerBtn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.mdc-button.mdc-button--touch.mdc-button--raised.access-btn"))
    )

    # Click the "Continuer" button
    continuerBtn.click()

    mdpBtn = wait.until(
        EC.element_to_be_clickable((By.ID, "btn-skip-password"))
    )

    # Click the "Utilisez votre mot de passe" button
    mdpBtn.click()

    mdpInput = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input.password-input"))  
    )

    # Fill the mdp input field
    mdp_a_Saisir = "iBSICHIXXX"  
    mdpInput.send_keys(mdp_a_Saisir)

    wait = WebDriverWait(driver,5)
    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "loginButton"))
    )

    # Click "Se connecter" button
    login_button.click()

    sleep(30)
     

finally:

# Close 
    driver.quit()