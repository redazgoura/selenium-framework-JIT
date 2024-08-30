from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random
import datetime

# Define the path to your msedgedriver
service = Service(executable_path=r'C:\edgedriver\msedgedriver.exe')
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options) # Define browser outside the try block

def humanize_delay(min_delay=2, max_delay=5):
    sleep(random.uniform(min_delay, max_delay))

def log_report(message):
    with open("reportCT03.txt", "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

try:
    log_report("Browser session started.")
    driver.maximize_window()
    log_report("Browser window maximized.")

    # Open the browser
    driver.get("https://www.jumia.ma/ordinateurs-accessoires-informatique/")
    log_report("Navigated to Jumia 'Informatique' category page via a direct link")
    
    # Verify the URL
    current_url = driver.current_url
    if current_url == "https://www.jumia.ma/ordinateurs-accessoires-informatique/":
        log_report("Successfully navigated to 'Informatique' category page via direct link.")
    else:
        log_report(f"Failed to navigate to 'Informatique' category page. Current URL: {current_url}")

    # Close pop-up window
    wait = WebDriverWait(driver, 10)
    pop_up_close = wait.until(
       EC.element_to_be_clickable((By.CSS_SELECTOR, "#pop .cls"))
    )

    humanize_delay()
    pop_up_close.click()
    log_report("Closed pop-up window.")

except Exception as e:
    log_report(f"An error occurred: {e}")

finally:
    sleep(10)
    log_report("Waiting for 10 seconds before closing the browser.")

    # Close the browser
    driver.quit()
    log_report("Browser session ended.")
