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

driver = setup_driver(executable_path=r'C:\edgedriver\msedgedriver.exe')

def humanize_delay(min_delay=2, max_delay=5):
    sleep(random.uniform(min_delay, max_delay))


def log_report(message):
    with open("reportCT13.txt", "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

 # scroll to the prefered product dynamically
def dynamic_scroll_to_element(xpath):
    increment = 700
    y = 0
    max_scroll = 7000  # Adjust acc ording to page length
    element = None  
    while y < max_scroll:
        driver.execute_script(f"window.scrollTo(0, {y})")
        time.sleep(1)  # Pause pour charger les éléments
        try:
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            if element:
                break
        except:
            y += increment
    log_report("Scroll down the webpage")
    return element 


def main():
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

        #  Wait for the banner to be present and then find the close button
        closeButton = WebDriverWait(driver, 20).until(
               EC.element_to_be_clickable((By.CLASS_NAME, 'cls')
            )
        )
        
        humanize_delay()
        # Click the close button
        closeButton.click()
        log_report("Closed banner.")

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
       
        # Click on a product 
        
        # Locate the specific <a> tag within the <article> element using both class and href attribute
        product_element = "//a[@href='/xiaomi-monitor-a22i-2145in-24w-max-75hz-aspect-ratio-169-64649885.html']/ancestor::article"
       
        productSelection = dynamic_scroll_to_element(product_element)
        
        if productSelection :
            log_report("Product found")

            # do a mouse hover on the product 
            product_mouse_hover = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, product_element)))
            
            humanize_delay()
            action = ActionChains(driver)

            #Performing the mouse hover action on the target element.
            action.move_to_element(product_mouse_hover).perform()

            # Creating object of an Actions class
            log_report("Mouse hover on 'Xiaomi Monitor' product.") 
        
            # Wait until the product page loads and find the add to cart button
            humanize_delay()

            # Wait until the product page loads and find the add to cart button
            addToCartButton = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH,"//a[@href='/xiaomi-monitor-a22i-2145in-24w-max-75hz-aspect-ratio-169-64649885.html']/ancestor::article//footer//button[@type='button' and contains(text(),'Ajouter au panier')]"))
            )

            humanize_delay()
            # Click the button
            addToCartButton.click()
            log_report("Boutton 'Ajouter au panier' Clicked")

            # Wait for the "Panier" button to be clickable
            panier_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/cart/') and contains(., 'Panier')]"))
            )

            time.sleep(5)
            log_report('Clicking the "Panier" button on the navbar')
            # Click the "Panier" button
            panier_button.click()
            log_report("Successfully clicked the 'Panier' button")    
        
        else :
            log_report("Product not found !!!!")            
        
    except Exception as e:
        log_report(f"An error occurred: {e}")

    finally:
        # Wait before closing the window
        sleep(30)
        log_report("Waiting for 10 seconds before closing the browser.")

        # Close the browser
        driver.quit()
        log_report("Browser session ended.")
       

if __name__ == "__main__":
    main()
