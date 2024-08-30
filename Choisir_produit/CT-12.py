from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import random
import datetime
import time

def setup_driver(executable_path):
    service = Service(executable_path=executable_path)
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(service=service, options=options)
    return driver

def humanize_delay(min_delay=2, max_delay=5):
    sleep(random.uniform(min_delay, max_delay))

def log_report(message):
    with open("reportCT12.txt", "a") as f:
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
        # Creating object of an Actions class
        action = ActionChains(driver)

        #Performing the mouse hover action on the target element.
        action.move_to_element(informatique_cat).perform()
        log_report("Mouse hover on 'Informatique' category.")


        productSelction = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Pc Gamer et composants']"))
        )

        humanize_delay()
        ActionChains(driver).move_to_element(productSelction).click().perform()
        log_report("Click on 'Pc Gamer et composants' products")


    # Verify if the click was successful by checking the URL or presence of an element on the target page
        try:
            WebDriverWait(driver, 10).until(
                EC.url_contains("/mlp-informatique-pc-gamer-et-composants/")
            )
            log_report("Successfully navigated to 'Pc Gamer et composants' sub-category page.")
        except Exception as e:
            log_report(f"Failed to navigate to 'Pc Gamer et composants' sub-category page: {e}")
    
        # scroll to the prefered product
        driver.execute_script("window.scrollTo(0, 200)")
        log_report("Scroll down to the dropdown menu")

        # Click the parent div to open the dropdown menu
        parent_div = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//label[@for='dpdw-sort']"))
        )
        # Waiting for the dropdown to appear 
        log_report("Waiting for the dropdown to appear...")
        
        humanize_delay()
        parent_div.click()
        log_report("Clicking the parent div to open the dropdown to execute the sorting")

        # Click the "Les mieux notés" element
        les_mieux_notes = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Les mieux notés')]"))
        )
        humanize_delay()
        les_mieux_notes.click()
        log_report("Click on 'Les mieux notés' sorting item")

        # scroll to the prefered product
        driver.execute_script("window.scrollTo(0, 600)")
        log_report("Scroll down the webpage")

    # Verify if the click was successful by checking the URL or presence of an element on the target page
         # Wait for the element to be present in the DOM and visible 
        productSelction = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/ecran-27-pouces-full-hd-ips-75hz-led-freesync-gaming-monitor-s2721hn-dell-mpg963687.html']"))
        )

        humanize_delay()
        ActionChains(driver).move_to_element(productSelction).click().perform()
        log_report("Click on 'DELL Écran 27 pouces Full HD, IPS, 75Hz LED FreeSync Gaming Monitor (S2721HN)' product")

    # Verify if the click was successful by checking the URL or presence of an element on the target page
        try:
            WebDriverWait(driver, 10).until(
                EC.url_contains("/ecran-27-pouces-full-hd-ips-75hz-led-freesync-gaming-monitor-s2721hn-dell-mpg963687.html")
            )
            log_report("Successfully navigated to 'DELL Écran 27 pouces Full HD, IPS, 75Hz LED FreeSync Gaming Monitor (S2721HN)' product page.")
        except Exception as e:
            log_report(f"Failed to navigate to 'DELL Écran 27 pouces Full HD, IPS, 75Hz LED FreeSync Gaming Monitor (S2721HN)' product page: {e}")
    
    

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
