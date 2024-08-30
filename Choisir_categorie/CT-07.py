from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random
import datetime

def setup_driver(executable_path):
    service = Service(executable_path=executable_path)
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(service=service, options=options)
    return driver

def humanize_delay(min_delay=2, max_delay=5):
    sleep(random.uniform(min_delay, max_delay))

def log_report(message):
    with open("reportCT01.txt", "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

def main():
    driver = setup_driver(executable_path=r'C:\edgedriver\msedgedriver.exe')

    try:
        log_report("Browser session started.")
        driver.maximize_window()
        log_report("Browser window maximized.")

        # Open the browser
        driver.get("https://www.jumia.ma/")
        log_report("Navigated to Jumia homepage.")
        
        # Close pop-up window
        wait = WebDriverWait(driver, 10)
        pop_up_close = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#pop .cls"))
        )

        humanize_delay()
        pop_up_close.click()
        log_report("Closed pop-up window.")

        # Click the link to "Informatique" category
        informatique_cat = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/ordinateurs-accessoires-informatique/']//span[text()='Informatique']"))
        )
        
        humanize_delay()
        informatique_cat.click()
        log_report("Clicked on 'Informatique' category.")


        # Verify if the click was successful by checking the URL or presence of an element on the target page
        try:
            WebDriverWait(driver, 10).until(
                EC.url_contains("/ordinateurs-accessoires-informatique/")
            )
            log_report("Successfully navigated to 'Informatique' category page.")
        except Exception as e:
            log_report(f"Failed to navigate to 'Informatique' category page: {e}")


    except Exception as e:
        log_report(f"An error occurred: {e}")

    finally:
        # Wait before closing the window
        sleep(10)
        log_report("Waiting for 10 seconds before closing the browser.")

        # Close the browser
        driver.quit()
        log_report("Browser session ended.")

if __name__ == "__main__":
    main()
