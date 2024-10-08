import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import numpy as np
from datetime import datetime

# Get the current time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Print the current time
print("Current time:", current_time)

webdriver = webdriver.Edge()
lock = threading.Lock()
current_balance = 15000
count_finished = 0
original_count = 0
original_amount_deposited = 0
all_rest = False


class BettingBot:
    def __init__(self, username, password, amount_to_use, average_odd, number_of_trials, threads):
        global current_balance, original_amount_deposited
        current_balance = amount_to_use
        original_amount_deposited = current_balance
        self.username = username
        self.password = password
        self.amount_to_use = amount_to_use
        self.average_odd = average_odd
        self.number_of_trials = number_of_trials
        self.driver = webdriver
        self.index = 0
        self.threads = threads

    def get_odd_value(self):
        try:
            odd_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='betItem-odd']"))
            )
            return float(odd_element.text)
        except Exception as e:
            print(f"Error getting odd value: {e}")
            return None

    def stake_distribution_starting_stake(self):
        all_stakes = [50]
        starting_stake = all_stakes[0]

        for count in range(2, self.number_of_trials + 1):
            new_stake = int(
                (np.sum(all_stakes) + (starting_stake * (self.average_odd - 1) * count)) / (self.average_odd - 1))
            all_stakes.append(new_stake)

        num = (self.amount_to_use + (self.amount_to_use * 0.15)) / np.sum(all_stakes)
        all_stakes = [int(stake * num) for stake in all_stakes]

        number_of_threads = self.threads
        win = ((all_stakes[0] * self.average_odd) - all_stakes[0])
        duration = (24 * 60 * 60) / 30
        print(
            f"Total: {sum(all_stakes)}       win: {win}     increase: {(win / sum(all_stakes)) + 1}     monthly: {((win / sum(all_stakes)) + 1) ** duration}    profit: {(((win / sum(all_stakes)) + 1) ** duration) * self.amount_to_use}")

        return all_stakes

    def fill_input_field(self, locator, element_id, value):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((locator, element_id)))
        element.clear()
        element.send_keys(value)

    def click_number(self, num):
        if int(num) == 0:
            num = "1"
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f"button[data-testid='keyboard-button-{num}']"))
        )
        button.click()

    def handle_login(self):
        self.driver.get("https://sports.bet9ja.com/event/465448155")
        # self.driver.get("https://vpnmasterpro.com/check-ip/")

        login_button = WebDriverWait(self.driver, 4).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-primary-m.btn-login'))
        )
        login_button.click()

        self.fill_input_field(By.ID, "username", self.username)
        self.fill_input_field(By.ID, "password", self.password)

        login_button = WebDriverWait(self.driver, 4).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-primary-l.mt20'))
        )
        login_button.click()

        time.sleep(3)
        print('Login successful')

    def switch_to_simulate_mode(self):
        try:
            time.sleep(5)
            switch_label = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "label[for='switch-on-off']"))
            )
            switch_label.click()
            print("Switched to 'Simulate'")
            time.sleep(3)
        except:
            print("No need to switch: it failed")

    def open_speed_menu(self):
        iframe = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "iframe"))
        )
        self.driver.switch_to.frame(iframe)
        try:
            speed_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.sc-kTYLvb.BAThW.MenuButton"))
            )
            speed_button.click()
            print("Opened speed menu")

            turbo_speed_option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-testid='turbo-normal']"))
            )
            turbo_speed_option.click()
            print("Selected 'Turbo speed'")
        except:
            print("No need to click on Turbo")

    def click_ok_continue(self):
        try:
            # Locate the "OK Continue" button using its title attribute
            ok_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@title='Okay' and contains(.,'OK Continue')]"))
            )
            # Click the button
            ok_button.click()
            print("Clicked 'OK Continue' button")
        except Exception as e:
            print(f"Error clicking 'OK Continue' button: ")

    def place_bet(self, stake_list, index):
        print(f"Stake: {stake_list[index]} with index: {index}")
        time.sleep(2)
        try:
            # Locate the stake input field container
            stake_div = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='input-field']"))
            )
            print("Stake field located")

            # Locate and click the remove button (cancel existing stake input)
            remove_button = stake_div.find_element(By.CSS_SELECTOR, "svg[data-testid='input-field-remove']")
            remove_button.click()
            print("Remove button clicked")

        except Exception as e:
            print(f"Error during stake input removal: ")

        time.sleep(2)
        print("virtual")
        stake_div.click()

        print("Inputting stake value")
        time.sleep(2)
        for digit in str(stake_list[index]):
            self.click_number(digit)
            time.sleep(1)

        time.sleep(2)
        place_bet_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='placeBetButton']"))
        )
        place_bet_button.click()
        print("Clicked 'Place Bet' button")
        time.sleep(3)

    def refresh_and_switch(self):
        self.driver.refresh()
        try:
            self.pick_game()
        except:
            print("Game already picked no need to re-pick")
        self.switch_to_simulate_mode()

    def pick_game(self):
        time.sleep(7)
        try:
            # XPath to find the accordion item containing the desired text
            accordion_xpath = ('//div[contains(@class, "accordion-item--open") and .//p[contains(text(), "Odd or even '
                               'total number of goals after Full time (FT)")]]')

            # Find the element with the specified XPath
            accordion_element = self.driver.find_element(By.XPATH, accordion_xpath)
            # Locate the odd odds element within the accordion item using XPath
            odd_odds_element = accordion_element.find_element(By.XPATH,
                                                              './/div[@class="market-item"][div/span[text('
                                                              ')="Odd"]]//div[@class="market-odd"]')

            # Locate the even odds element within the accordion item using XPath
            even_odds_element = accordion_element.find_element(By.XPATH,
                                                               './/div[@class="market-item"][div/span[text('
                                                               ')="Even"]]//div[@class="market-odd"]')
            # odd_odds_element.click()
        except:
            print("I input myself")

    def handle_bet_result(self, stake_list, index):
        global current_balance
        time.sleep(10)
        try:
            won_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "p.won"))
            )
            value = stake_list[index]
            sum_of_index = sum(stake_list[:index + 1])
            gain = (value * self.average_odd)
            self.amount_to_use += (gain - sum_of_index)
            print("It won the bet")
            current_balance += (gain - value)
            print(f"Current balance: {current_balance}")
            return True
        except Exception:
            print("Lost the match")
            current_balance -= stake_list[index]
            print(f"Current balance: {current_balance}")
            return False

    def run(self):
        self.handle_login()
        self.pick_game()
        self.switch_to_simulate_mode()
        self.open_speed_menu()

    def go(self):
        global count_finished, all_rest, current_balance
        while True:
            try:
                stake_list = self.stake_distribution_starting_stake()
                if not stake_list:
                    continue  # Skip if no stakes were returned
                else:
                    print(stake_list)

                with lock:
                    time.sleep(2)  # very important
                    if all_rest:
                        print(f"ready to re-bet :This thread returned")
                        self.index = 0
                        return
                    self.place_bet(stake_list, self.index)

                    num = 3
                    try:
                        if self.handle_bet_result(stake_list, self.index):
                            percentage_loss = 1  # 3.16
                            if self.index >= num and (abs(current_balance - original_amount_deposited) <= ((percentage_loss / 100) * original_amount_deposited)):
                                print(f"First statement: {self.index >= num}  and second statement: {self.index >= num + 1}")
                                print(
                                    f"Winning thread Index is >= {num} and current balance {current_balance} > {original_amount_deposited} and profit is {current_balance - original_amount_deposited}")
                                if current_balance < original_amount_deposited:
                                    print(f"This is a maximum loss of {current_balance - original_amount_deposited}")
                                all_rest = True
                            self.index = 0
                        else:

                            self.index += 1

                            if self.index >= self.number_of_trials - 1:
                                self.index -= 1
                                sum_of_index = sum(stake_list[:self.index])
                                self.amount_to_use -= sum_of_index
                                self.index = 0
                            # if self.amount_to_use < 15000:
                            #     self.number_of_trials = 5
                            #     print("Amount is less than 15000")

                        done_button = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='game-done']"))
                        )
                        done_button.click()
                        print("Clicked on the 'Done' button successfully.")

                    except Exception as e:
                        print(f"Interesting problem 1")
                        self.index -= 1
                        current_balance += stake_list[self.index]
                        print(f"did current balance change:  {current_balance}")
                        self.click_ok_continue()
                        print("continue")
                        continue
                if self.index >= num + 2:
                    if current_balance < original_amount_deposited:
                        print(f"Now we have a Terrible loss of {current_balance - original_amount_deposited}")
                    all_rest = True
                    self.index = 0

                if count_finished <= 3 <= self.index:
                    print("This is a failed hope, restart over again")
                    print(
                        f"Failed thread Index is >= {num} and current balance {current_balance} > {original_amount_deposited} and profit is {current_balance - original_amount_deposited}")
                    if current_balance < original_amount_deposited:
                        print(f"This is a Terrible loss of {current_balance - original_amount_deposited}")
                    all_rest = True
                    self.index = 0

                if current_balance > original_amount_deposited:
                    print(
                        f"Account balance is greater than original amount {current_balance} > {original_amount_deposited} and profit is {current_balance - original_amount_deposited}")
                    all_rest = True

                if self.index == 0:
                    count_finished -= 1
                    print("Thread is going to sleep")
                    print(f"Number of thread remaining: {count_finished}")
                    while count_finished > 0 and (not all_rest):
                        time.sleep(1)
                    print("ready to re-bet")
                    time.sleep(3)
                    print("finishing 3 seconds")
                    count_finished = original_count

            except Exception as e:
                with lock:
                    print(f"Interesting problem: 2")
                    self.click_ok_continue()


def run_multiple_bots(num_bots):
    global count_finished, original_count, original_amount_deposited, current_balance, all_rest
    count_finished = num_bots
    original_count = count_finished
    threads = []
    for i in range(num_bots):
        bot = BettingBot("ezekielgadzama", "Ezekiel23", current_balance, 1.88, 7, num_bots)
        thread = threading.Thread(target=bot.go)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    original_amount_deposited = current_balance
    all_rest = False
    print("Running again")
    run_multiple_bots(num_bots)


if __name__ == "__main__":
    num_bots = 10
    boter = BettingBot("ezekielgadzama", "Ezekiel23", current_balance, 1.88, 7, num_bots)
    boter.run()
    run_multiple_bots(num_bots)  # Change this number to create more or fewer bots
