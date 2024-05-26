import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def find_and_fill_input(driver, xpath, input_value, input_name):
    """
    Locates an input field by XPath, clears it, and enters the provided value.

    Args:
        driver: The Selenium WebDriver instance.
        xpath: The XPath locator for the input field.
        input_value: The value to enter into the field.
        input_name: A descriptive name for the input field.
    """
    try:
        input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        input_element.clear()
        input_element.send_keys(input_value)
        print(f"{input_name.capitalize()} input value: {input_element.get_attribute('value')}")
    except TimeoutException:
        print(f"Error: Timeout waiting for {input_name} field.")

def click_element(driver, xpath):
    """
    Locates an element by XPath and clicks it if it's clickable.
    """
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()
    except TimeoutException:
        print(f"Error: Timeout waiting for element to be clickable: {xpath}")


# Driver setup
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=chrome_options)

# Credentials
username = "7042280970"
password = "Morenigbade1$"

# Navigation and login
driver.get("https://www.sportybet.com/ng/")

username_xpath = '//*[@id="j_page_header"]/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/input'
password_xpath = '//*[@id="j_page_header"]/div[1]/div/div[1]/div[1]/div[2]/div[3]/div[1]/input'
login_xpath = '//*[@id="j_page_header"]/div[1]/div/div[1]/div[1]/div[2]/div[3]/div[1]/button'

find_and_fill_input(driver, username_xpath, username, "username")
find_and_fill_input(driver, password_xpath, password, "password")
click_element(driver, login_xpath)
print("Login susss")

print(driver.title)

# Wait and close (adjust as needed)
time.sleep(30)
driver.quit()
