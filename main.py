import time
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException




# Driver setup
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-popup-blocking')
chrome_options.add_argument('--disable-notifications')


driver = webdriver.Chrome(options=chrome_options)

# Credentials
username = "ezekielgadzama"
password = "Ezekiel23"

# Navigation and login
driver.set_window_size(1920, 1080)
driver.get("https://sports.bet9ja.com/")

username_id = 'username'
password_id = 'password'
login_popup_selector = '#header_item > div > div > div > div.h-ml__acc > div:nth-child(3) > div.btn-primary-m.btn-login'
login_xpath = '//*[@id="header_item"]/div/div/div/div[2]/div[3]/div[2]/div[1]/div[3]'

# Retry logic to handle StaleElementReferenceException

time.sleep(5)
max_retries = 3
# for attempt in range(max_retries):
#     try:
#         # Wait for the element to be clickable
#         element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, login_popup_selector)))
#         element.click()
#         break  # Exit loop if click is successful
#     except StaleElementReferenceException:
#         if attempt < max_retries - 1:
#             continue  # Retry
#         else:
#             raise  # Reraise the last exception



try:

    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, login_popup_selector)))
    element.click()
    # Wait for the input field to be visible
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="username"]'))
    )

    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))
    )

    # Click the input field
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
