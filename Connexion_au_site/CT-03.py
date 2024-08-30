from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep
import random

# renseigner le chemin de votre msedgedriver dans executable_path
service = Service(executable_path=r'C:\edgedriver\msedgedriver.exe')
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options) # Define browser outside the try block


def humanize_delay(min_delay=2.0, max_delay=5.0):
    sleep(random.uniform(min_delay, max_delay))

try:
    driver.maximize_window()

    # Open the browser
    driver.get("https://www.jumia.ma")
    
    # Wait for the element to be clickable
    wait = WebDriverWait(driver, 10)
    button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#pop .cls"))
    )

    humanize_delay()
    # Click the button
    button.click()
    

    wait = WebDriverWait(driver, 10)
    dropdown_trigger = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='dpdw-login']"))
    )

    humanize_delay()
    # Click the dropdown trigger
    dropdown_trigger.click()
   


    wait = WebDriverWait(driver, 10)
    login_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#dpdw-login-box a.btn._prim"))
    )
    humanize_delay()
    login_button.click()
    

    emailInput = wait.until(
        EC.visibility_of_element_located((By.ID, "input_identifierValue"))  
    )

    # Fill the email input field
    
    emailAddress1 = "redazr1997@gmail"
    #emailAddress2 = "redazr@"  
    #emailAddress3 = "redazr"  
    
    humanize_delay()  
    emailInput.send_keys(emailAddress1)
  
    
    wait = WebDriverWait(driver, 10)
    continuerBtn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.mdc-button.mdc-button--touch.mdc-button--raised.access-btn"))
    )

    humanize_delay()
    # Click the "Continuer" button
    continuerBtn.click()
     
finally:

    sleep(30)

    # Close 
    driver.quit()