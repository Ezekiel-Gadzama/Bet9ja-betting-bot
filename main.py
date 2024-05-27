import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Driver setup
firefox_options = Options()
firefox_options.headless = True

driver = webdriver.Firefox(options=firefox_options)

# Credentials
username = "ezekielgadzama"
password = "Ezekiel23"

# Navigation and login
driver.get("https://sports.bet9ja.com/")

username_id = 'username'
password_id = 'password'
login_popup_selector = '#header_item > div > div > div > div.h-ml__acc > div:nth-child(3) > div.btn-primary-m.btn-login'

try:
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, login_popup_selector)))
    element.click()

    # Wait for the input field to be visible
    username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="username"]')))
    password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))

    # Input credentials
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Click login button
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#header_item > div > div > div > div.h-ml__acc > div:nth-child(3) > div.login_popup.open > div.form > div.btn-primary-l.mt20')))
    login_button.click()
    print("Login successful")

    # Add more interactions as needed...

except TimeoutException:
    print("Timeout occurred while waiting for elements.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Keep the browser open for inspection
    input("Press Enter to close the browser...")
    driver.quit()
