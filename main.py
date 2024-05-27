import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    StaleElementReferenceException, 
    TimeoutException, 
    NoSuchElementException, 
    WebDriverException
)

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Driver setup
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument('--disable-popup-blocking')
chrome_options.add_argument('--disable-notifications')

# Note: Update the ChromeDriver path to be Linux-friendly
chrome_driver_path = "/usr/bin/chromedriver"  # Make sure chromedriver is installed and in this path
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Credentials
username = "ezekielgadzama"
password = "Ezekiel23"

try:
    # Set window size and open the URL
    driver.set_window_size(1920, 1080)
    logger.info("Navigating to Bet9ja...")
    driver.get("https://sports.bet9ja.com/")
    logger.info("Page loaded.")

    # Check if the error message is displayed
    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "This site can’t be reached")]'))
        )
        if error_message:
            logger.error("This site can’t be reached")
            print("This site can’t be reached")
            driver.quit()
            exit()
    except TimeoutException:
        logger.info("No error message found, proceeding with login.")

    username_id = 'username'
    password_id = 'password'
    login_popup_selector = '#header_item > div > div > div > div.h-ml__acc > div:nth-child(3) > div.btn-primary-m.btn-login'
    login_xpath = '//*[@id="header_item"]/div/div/div/div[2]/div[3]/div[2]/div[1]/div[3]'

    # Wait for login popup and click
    logger.info("Waiting for login popup to be clickable...")
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, login_popup_selector)))
    element.click()
    logger.info("Login popup clicked.")

    # Wait for username and password fields to be visible
    logger.info("Waiting for username field...")
    username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="username"]')))
    logger.info("Username field found.")

    logger.info("Waiting for password field...")
    password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))
    logger.info("Password field found.")

    # Enter credentials
    logger.info("Entering username...")
    username_field.click()
    time.sleep(1)
    username_field.send_keys(username)
    logger.info("Username entered.")

    logger.info("Entering password...")
    password_field.click()
    time.sleep(1)
    password_field.send_keys(password)
    logger.info("Password entered.")

    # Click login button
    logger.info("Waiting for login button to be clickable...")
    login_button_selector = '#header_item > div > div > div > div.h-ml_acc > div:nth-child(3) > div.login_popup.open > div.form > div.btn-primary-l.mt20'
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, login_button_selector)))
    login_button.click()
    logger.info("Login button clicked.")

    # Wait for some time to ensure login is processed
    time.sleep(5)
    logger.info("Login process completed.")

except TimeoutException as te:
    logger.error(f"TimeoutException: {te}")
except StaleElementReferenceException as sere:
    logger.error(f"StaleElementReferenceException: {sere}")
except NoSuchElementException as nse:
    logger.error(f"NoSuchElementException: {nse}")
except WebDriverException as wde:
    logger.error(f"WebDriverException: {wde}")
except Exception as e:
    logger.error(f"An unexpected error occurred: {e}")
finally:
    input("Press Enter to close the browser...")
    driver.quit()
    logger.info("Browser closed.")
