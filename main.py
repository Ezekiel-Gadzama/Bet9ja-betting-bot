import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

# Driver setup
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument('--disable-popup-blocking')
chrome_options.add_argument('--disable-notifications')

chrome_driver_path = "C:\\Program Files\\chromedriver"
driver = webdriver.Chrome(options=chrome_options)

# Navigation and error check
driver.set_window_size(1920, 1080)
try:
    driver.get("https://sports.bet9ja.com/")
    print("loaded completely")
except:
    print("loading page failed")

# Check for "This site can’t be reached" error
try:
    error_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(), \"This site can’t be reached\")]"))
    )
    print("found")
    if error_element:
        print("Page can't be reached")
        driver.quit()
        exit()
except TimeoutException:
    # Proceed with normal flow if the error element is not found
    pass

# Credentials
username = "ezekielgadzama"
password = "Ezekiel23"

# Navigation and login
username_id = 'username'
password_id = 'password'
login_popup_selector = '#header_item > div > div > div > div.h-ml__acc > div:nth-child(3) > div.btn-primary-m.btn-login'
login_xpath = '//*[@id="header_item"]/div/div/div/div[2]/div[3]/div[2]/div[1]/div[3]'

time.sleep(5)
max_retries = 3
print("time to login")

try:
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, login_popup_selector)))
    element.click()
    # Wait for the input fields to be visible
    username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="username"]')))
    password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))
    
    # Enter credentials
    username_field.click()
    time.sleep(3)
    username_field.click()
    username_field.send_keys(username)
    
    password_field.click()
    time.sleep(3)
    password_field.click()
    password_field.send_keys(password)
    
    login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#header_item > div > div > div > div.h-ml_acc > div:nth-child(3) > div.login_popup.open > div.form > div.btn-primary-l.mt20')))
    login.click()

    # Add more interactions as needed...

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Keep the browser open for inspection
    input("Press Enter to close the browser...")
    driver.quit()
