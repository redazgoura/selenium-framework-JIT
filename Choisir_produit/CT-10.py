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
    with open("reportCT10.txt", "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

try:
    log_report("1.Browser session started.")
    driver.maximize_window()
    log_report("2.Browser window maximized.")

    # Open the browser
    driver.get("https://www.jumia.ma/")
    log_report("3.Navigated to Jumia website.")
    
    # Close pop-up window
    wait = WebDriverWait(driver, 10)
    pop_up_close = wait.until(
       EC.element_to_be_clickable((By.CSS_SELECTOR, "#pop .cls"))
    )

    humanize_delay()
    pop_up_close.click()
    log_report("4.Closed pop-up window.")

    # Searching Input
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "fi-q"))
    )

    humanize_delay()
    # Fill the search input field
    search_input.send_keys("msi")
    log_report("5.Entered 'msi' product in the search input field.")
    
    # Verify the input field contains the expected text
    if search_input.get_attribute("value") == "msi":
        log_report("6.Search input field contains the (msi) keyword.")
    else:
        log_report("6.Search input field does not contain the right keyword.")
    
    # Wait for the search button to be clickable
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "form#search button.btn._prim._md.-mls.-fsh0"))
    )
    
    humanize_delay()
    # Click the search button
    search_button.click()
    log_report("7.Clicked the search button.")

    # Verify if the click was successful by checking the URL or presence of an element on the search results page
    try:
        WebDriverWait(driver, 10).until(
            EC.url_contains("/catalog/?q=msi")
        )
        log_report("8.Successfully navigated to search results page.")
    except Exception as e:
        log_report(f"8.Failed to navigate to search results page: {e}")

    product_xpath = "//a[@href='/msi-katana-17-b13vgk-16gb1tb-i9-13900h-rtx-40708gb-gddr6-black-azerty-remis-a-neuf-65226237.html']"
    product_link = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, product_xpath))
    )
    product_link.click()


finally:
    sleep(10)
    log_report("9.Waiting for 10 seconds before closing the browser.")

    # Close the browser
    driver.quit()
    log_report("10.Browser session ended.")
