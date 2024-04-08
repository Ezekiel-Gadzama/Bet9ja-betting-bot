from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import keyboard
from selenium.webdriver.common.keys import Keys

def get_match_info(driver):
    try:
        # Wait for the table to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'sports-table__time')))
        
        # Find all match info elements
        match_elements = driver.find_elements(By.CSS_SELECTOR, '.table-f')
        print("Hello: ",len(match_elements))
        # Extract information from each match
        for match in match_elements:
            try:
                # Adding explicit wait for time element
                time_element = WebDriverWait(match, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'sports-table__time'))).find_element(By.TAG_NAME, 'span').text
                home_team = match.find_element_by_class_name('sports-table__home').text
                
                away_team = match.find_element_by_class_name('sports-table__away').text.text
                
                # Get odd/even odds
                odds_elements = match.find_elements(By.CLASS_NAME, 'sports-table__odds-item')
                odd_odds = odds_elements[0].text
                even_odds = odds_elements[1].text
                
                # Output match info
                print(f"Time: {time_element}, Teams: {home_team} vs {away_team}, Odd Odds: {odd_odds}, Even Odds: {even_odds}")
            except NoSuchElementException:
                print("An error occurred: sports-table__time element not found for a match.")
                
    except Exception as e:
        print("And error occurred:", e)



def get_account_balance(driver):
    try:
        # Wait for the balance element to be visible
        balance_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".acc-dd__btn-right .myaccount__balance"))
        )
        # Get the text content of the balance element
        account_balance = balance_element.text
        return account_balance
    except NoSuchElementException:
        return "Balance element not found"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Github credentials
username = "ezekielgadzama"
password = "Ezekiel23"

# Initialize Selenium WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to the Bet9ja website
    driver.get("https://sports.bet9ja.com/sport/soccer/1")

    # Wait for the login button to be clickable
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-primary-m.btn-login'))
    )

    # Click on the login button
    login_button.click()

    # Find the username field
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )

    # Input your username
    username_input.send_keys(username)

    # Find the password field
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "password"))
    )

    # Input your password
    password_input.send_keys(password)

    # Click on the login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-primary-l.mt20'))
    )
    login_button.click()

    # Find and click on the "Upcoming" tab
    upcoming_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//li[contains(text(), "Upcoming")]'))
    )
    upcoming_tab.click()

    odd_even_tab = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//td[contains(text(), "Odd/Even")]'))
    )
    odd_even_tab.click()


    # Get account balance
    balance = get_account_balance(driver)
    print("Account Balance:", balance)
    get_match_info(driver)


    print("Press 'x' key to close the browser window...")
    keyboard.wait('x')
    print("Exiting...")



finally:
    # Close the browser
    driver.quit()
