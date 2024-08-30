from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep
import random
import imaplib
import email
import re

# renseigner le chemin de votre msedgedriver dans executable_path
service = Service(executable_path=r'C:\edgedriver\msedgedriver.exe')
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options) # Define browser outside the try block

# delay time to humanize selenium interaction with the application 
def delayTime(min_delay= 2, max_delay = 5):
    sleep(random.uniform(min_delay, max_delay))

# get get_otp_from_email function 
def get_otp_from_email(email_user, email_password, email_server="imap.gmail.com"):

    mail = imaplib.IMAP4_SSL(email_server)
    mail.login(email_user, email_password)
    mail.select("inbox")  # Sélectionner la boîte de réception

    # search all emails
    status, messages = mail.search(None, 'UNSEEN')
    email_ids = messages[0].split()
    
    otp = None
    if email_ids:
        for e_id in email_ids:
            # Get the email
            status, msg_data = mail.fetch(e_id, '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    if msg.is_multipart():
                        for part in msg.walk():
                            if part.get_content_type() == "text/plain":
                                email_body = part.get_payload(decode=True).decode()
                                # Recherche du code OTP de 4 chiffres
                                otp_match = re.search(r'\b\d{4}\b', email_body)
                                if otp_match:
                                    otp = otp_match.group(0)
                                    break
                    else:
                        email_body = msg.get_payload(decode=True).decode()
                        # Recherche du code OTP de 4 chiffres
                        otp_match = re.search(r'\b\d{4}\b', email_body)
                        if otp_match:
                            otp = otp_match.group(0)
                            break
            if otp:
                break

    # Logout
    mail.logout()
    
    return otp

try:
    driver.maximize_window()

    # Open the browser
    driver.get("https://www.jumia.ma")
    
    # Wait for the element to be clickable
    wait = WebDriverWait(driver, 10)
    button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#pop .cls"))
    )

    delayTime()
    # Click the button
    button.click()

    wait = WebDriverWait(driver, 10)
    dropdown_trigger = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='dpdw-login']"))
    )

    delayTime()
    # Click the dropdown trigger
    dropdown_trigger.click()


    login_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#dpdw-login-box a.btn._prim"))
    )

    delayTime()
    login_button.click()

    emailInput = wait.until(
        EC.visibility_of_element_located((By.ID, "input_identifierValue"))  
    )

    # Fill the email input field
    emailAddress = "redazr1997@gmail.com"  
    delayTime()
    emailInput .send_keys(emailAddress)

    continuerBtn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.mdc-button.mdc-button--touch.mdc-button--raised.access-btn"))
    )

    # Click the "Continuer" button
    continuerBtn.click()

    mdpBtn = wait.until(
        EC.element_to_be_clickable((By.ID, "btn-skip-password"))
    )

    delayTime()
    # Click the "Utilisez votre mot de passe" button
    mdpBtn.click()

    mdpInput = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input.password-input"))  
    )

    # Fill the mdp input field
    mdp_a_saisir = "APSYCHIC@"  
    mdpInput.send_keys(mdp_a_saisir)

    wait = WebDriverWait(driver,10)
    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "loginButton"))
    )

    delayTime()
    # Click "Se connecter" button
    login_button.click()    

    # Utilisation
    email_user = 'redazr1997@gmail.com'
    email_password = 'ZGOUR@270597'

    otp = get_otp_from_email(email_user, email_password)
    if otp:
        print(f"The OTP is: {otp}")
    else:
        print("No OTP found.")

finally:
    
    sleep(100)

    # Close 
    driver.quit()