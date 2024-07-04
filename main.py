from datetime import datetime, timedelta
import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import webdriver
import numpy as np
import pytz
import math
import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import string
import logging
import sys
import os
import re

# Initialize lists to store data
username = "ezekielgadzama"
password = "Ezekiel23"
number_of_trials = 9  # advice to use a minimum of 5
potential_monthly_Profit = 60
amount_to_use = 230900
# can not be less than [5: 7085], [6: 16020], [7: 35567], [8: 78210], [9: 171121], [10: 373439], [11:
betType = "Goal"  # 'Goal', 'Corner', 'Win team'
starting_stake = 100  # can not be less than 100
#  (all minimum amount)
average_odd = 1.85
Default_account_balance = 0
sum_of_all_profit_made = 0
original_amount_to_use = amount_to_use
BotPassword = None
current_amount = amount_to_use
listOfNotFoundMatchIndex = []
# fullname = input("Enter Full name: ")
# username = input("Enter bet9ja username: ")
# password = input("Enter bet9ja password: ")
# number_of_trials = int(input("Enter number of trials (minimum 5): "))
# potential_monthly_profit = float(input("Enter potential monthly profit: "))
# amount_to_use = int(input("Enter amount to use: "))
# recipient2 = input("Enter your email: ")

log_file = 'app.log'
if os.path.exists(log_file):
    os.remove(log_file)
# Configure root logger to capture warnings and errors from all libraries
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler('app.log', mode='a'),
                        logging.StreamHandler(sys.stdout)
                    ])

# Create a custom logger for your application
logger = logging.getLogger('my_app')
logger.setLevel(logging.INFO)


# Function to redirect print statements to logger
class StreamToLogger(object):
    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())

    def flush(self):
        pass


# Redirect stdout to the custom logger
sys.stdout = StreamToLogger(logger, logging.INFO)
sys.stderr = StreamToLogger(logger, logging.ERROR)

# Now both print statements and logging calls will go to the log file and console
logger.info("Logger initialized")

# Example print statement
print("This is a print statement")

###########################################################
recipients = ["ezekielgadzama17@gmail.com", "Adesijioyindamola71@gmail.com"
    , "adebolu.adewoyin@gmail.com", "blackboj@proton.me", "jimohnurudeen1256@gmail.com",
              "Kingsleyeke101@gmail.com", "Chrixs.barney@gmail.com",
              "oluabikoye@outlook.com"]  # Add more emails as needed
fullnames = ["Ezekiel John Gadzama", "Adesiji oyindamola boluwatife",
             "Adewoyin Daniel Adebolu", "Afeez Olanrewaju", "Jimoh Nurudeen Oluwaseun",
             "Kingsley Nkemdi Ekechukwu", "Christian Bassey", "Olu Abikoye"]  # Corresponding full names
original_amounts = [200000, 100000, 38500, 200000, 200000, 50000, 400000,
                    53200]  # Corresponding original amounts # other: 1041700
binomialBetBotEmail = "ezekielgadzama23@gmail.com"

#######################################################

# Shared flag to stop the thread
should_stop_event = threading.Event()


def send_profit_email(passwordT):
    global sum_of_all_profit_made
    global current_amount
    global original_amount_to_use
    global should_stop_event
    global BotPassword

    def generate_password():
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(10))
        return password

    while not should_stop_event.is_set():
        # if not passwordT:
        #     time.sleep(15)  # Sleep for 15 seconds for testing
        #     print("Sending profit message to clients")
        # else:
        #     print(
        #         "Generating password, contact the bot admin for your password\nPassword is only valid once every 30 days")
        #
        # sender_email = "afeezbolajiola@gmail.com"  # Replace with your email
        # password =  "mtek abgk sbwh zjce"  # Replace with your email password
        # smtp_server = "smtp.gmail.com"  # Replace with your SMTP server
        #
        # for recipient, fullname, original_amount in zip(recipients, fullnames, original_amounts):
        #     # Create message object
        #     message = MIMEMultipart()
        #     message["From"] = sender_email
        #     message["To"] = recipient
        #
        #     # Set subject based on passwordT
        #     if passwordT:
        #         message["Subject"] = f"{fullname} betting bot password"
        #         message_body = f"Password: {generate_password()}"
        #     else:
        #         message["Subject"] = f"{fullname} available balance"
        #         user_current_amount = (original_amount / original_amount_to_use) * current_amount
        #         binomial_commission = ((user_current_amount - original_amount) * 0.8)
        #         if binomial_commission < 0:
        #             binomial_commission = 0
        #         message_body = f"Total balance in account is: {user_current_amount}\nBinomial bet commission: {binomial_commission}\nYour available balance is: {(user_current_amount - binomial_commission)}"
        #
        #     # Attach message body
        #     message.attach(MIMEText(message_body, "plain"))
        #
        #     # Connect to SMTP server and send email
        #     with smtplib.SMTP_SSL(smtp_server, 465) as server:
        #         server.login(sender_email, password)
        #         server.sendmail(sender_email, recipient, message.as_string())
        #         server.sendmail(sender_email, binomialBetBotEmail, message.as_string())
        #         print(f"Message sent to {fullname}")

        if passwordT:
            days = 7
            print(f"Going to sleep for {days} days")
            time.sleep(60 * 60 * 24 * days)
            should_stop_event.set()
            print("Ready to stop, terminating thread one by one")


def start_email_thread(passwordT):
    email_thread = threading.Thread(target=send_profit_email, args=(passwordT,))
    email_thread.start()
    return email_thread


# Start the email sending thread
email_thread = start_email_thread(True)  # to be able to send profit email

# start_email_thread(True)  # To get password
# userPassword = input("Enter the one time bot password: ")
# if BotPassword != userPassword:
#     # Add the termination statement here
#     raise SystemExit("Incorrect password. Terminating the program.")


# Initialize the webdriver instances outside of Bet9jaBot class
driver = webdriver.Chrome()
live_score_driver = webdriver.Chrome()
# Define a lock and condition variable
pick_a_match_lock = threading.Lock()
won_lock = threading.Lock()
login_lock = threading.Lock()
place_bet_lock = threading.Lock()
live_score_lock = threading.Lock()
shareDistribution = None
globalCount = 0
globalDividedNumber = 290


class Bet9jaBot:
    def __init__(self, username, password, average_odd, amount_to_use, number_of_trials, starting_stake,
                 potential_monthly_Profit, betType, betting_odd_even):
        self.username = username
        self.password = password
        self.average_odd = average_odd
        self.amount_to_use = amount_to_use
        self.number_of_trials = number_of_trials
        self.starting_stake = starting_stake
        self.potential_monthly_Profit = potential_monthly_Profit
        self.betType = betType
        self.driver = driver
        self.live_score_driver = live_score_driver
        self.listOfAllOdds = []
        self.listOfAllAmountPlaced = []
        self.listOfAllMatch = []
        self.listOfAllLostMatch = []
        self.ListOfAllWinMatch = []
        self.last_match_time = "nothing"
        self.listOfAllMatchName = []
        self.listOfAllTotalFailedTrials = []
        self.betting_odd_even = betting_odd_even
        self.sleep_duration = 0
        self.match_starting_time = None
        self.find_match_time = None
        self.thread_trails = 0
        self.match_PST = False
        self.betTimes = 0

    def click_cancel_buttons(self, number_to_keep):
        value = False
        try:
            print("checking to cancel previous kept betting slip")
            # Find all the cancel buttons using the class name 'icon close'
            cancel_buttons = self.driver.find_elements(By.CSS_SELECTOR, '.betslip__match-item .icon.close')
            # Calculate the number of buttons to click
            number_to_click = len(cancel_buttons) - number_to_keep

            # Iterate through each cancel button and click on it, except the ones to keep
            for i, button in enumerate(cancel_buttons):
                if i < number_to_click:
                    button.click()
                    print("It cancelled a bet slip")
                    time.sleep(0.5)
                    value = True
            return value
        except:
            print("No pre-kept betting slip")

    def balance_clearance(self):
        global Default_account_balance
        """
        Calculates the required stake based on the given parameters.

        Args:
            number_of_trials (int): Number of betting trials.
            starting_stake (float): Initial stake amount.
            average_odd (float): Average odds for each bet.

        Returns:
            float: Required stake amount to achieve the desired total balance.
        """
        current_balance = self.get_account_balance()  # Parse as float
        Default_account_balance = current_balance
        print("Current Account Balance:", current_balance)
        self.listOfAllAmountPlaced.append(self.starting_stake)

        estimated_total_amount = self.total_account_balance_needed()
        amount_need = int(
            estimated_total_amount + 20)  # addition due to changes in odds

        # while current_balance < amount_need:
        #     print(f"Low account balance: Deposit {amount_need - current_balance:.2f} to your account")
        #     deposit = input("Enter 'D' if you have deposited: ")
        #     if deposit.upper() == 'D':
        #         current_balance = float(self.get_account_balance())  # Update the balance
        #     else:
        #         print("Please deposit the required amount.")
        return current_balance

    def num_bet_per_hour(self):
        def find_Profit_rate_per_day(potential_monthly_Profit):
            def f(x):
                return x ** 30 - potential_monthly_Profit

            a = 0  # Initial lower bound
            b = self.potential_monthly_Profit  # Initial upper bound
            tol = 1e-6  # Tolerance for stopping criterion

            while b - a > tol:
                c = (a + b) / 2
                if f(c) == 0:
                    return c  # Found exact solution
                elif f(a) * f(c) < 0:
                    b = c
                else:
                    a = c

            return (a + b) / 2

        max_dnumber_of_trials_per_day = 5
        account_needed = self.total_account_balance_needed()
        return math.ceil((((account_needed * find_Profit_rate_per_day(
            self.potential_monthly_Profit)) - account_needed) / (max_dnumber_of_trials_per_day * (
                (self.average_odd * self.starting_stake) - self.starting_stake))))

    def get_account_balance(self):
        try:
            # Wait for the balance element to be visible
            balance_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".acc-dd__btn-right .myaccount__balance"))
            )
            # Get the text content of the balance element
            account_balance = balance_element.text.replace(",", "")
            return float(account_balance)
        except NoSuchElementException:
            return "Balance element not found"
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def total_account_balance_needed(self):
        all_stakes = []
        all_stakes.append(self.starting_stake)
        for count in range(2, self.number_of_trials + 1):
            new_stake = int(
                (np.sum(all_stakes) + (self.starting_stake * (self.average_odd - 1) * count)) / (self.average_odd - 1))
            all_stakes.append(new_stake)
        print(all_stakes)
        return np.sum(all_stakes)

    def stake_distribution_starting_stake(self):

        all_stakes = []
        all_stakes.append(100)
        self.starting_stake = all_stakes[0]
        for count in range(2, self.number_of_trials + 1):
            new_stake = int(
                (np.sum(all_stakes) + (self.starting_stake * (self.average_odd - 1) * count)) / (self.average_odd - 1))
            all_stakes.append(new_stake)
        num = (self.amount_to_use + (self.amount_to_use * 0.15)) / np.sum(all_stakes)
        for i in range(len(all_stakes)):
            all_stakes[i] = int(all_stakes[i] * num)
        return all_stakes[0] + random.randint(0, 30)

    def fill_input_field(self, locator, element_id, value):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((locator, element_id)))
        element.clear()
        element.send_keys(value)

    def dataForEachMatch(self):
        self.driver.refresh()
        time.sleep(3)
        self.click_cancel_buttons(0)
        global last_match_time
        # Wait for the element to be clickable
        matchup_div = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="sports-view__nav"]'))
        )
        # Find the team names, league, and match description elements
        team_names_element = matchup_div.find_elements(By.CLASS_NAME, 'sports-viev__crumbs-link')[-1]
        league_element = matchup_div.find_elements(By.CLASS_NAME, 'sports-viev__crumbs-link')[-2]
        match_description_element = matchup_div.find_element(By.XPATH, './/a[@class="sports-viev__crumbs-link"]')

        # Extract text from the elements
        team_names = team_names_element.text.strip()
        league = league_element.text.strip()
        match_description = match_description_element.text.strip()

        print("Team Names:", team_names.split(' v '))
        print("League:", league)
        print("Match Description:", match_description)

        matchup_div = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="sports-view__bar md light table"]'))
        )

        date_time_element = matchup_div.find_elements(By.CLASS_NAME, 'table-cell.txt-gray.pl15')[-1]

        # Extract text from the date and time element
        last_match_time = date_time_element.text.strip().split("•")[0].strip()

        if self.betType == "Goal":
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
            # Click on the odd odds element
            if self.betting_odd_even == "O":
                odd_odds_element.click()
                # Extract the value of the odd odds
                odd_odds_value = float(odd_odds_element.text)
                # Print the value of the odd odds
                print("Goal Odd Odds Value:", odd_odds_value)
                self.listOfAllOdds.append(odd_odds_value)
            else:
                # Click on the even odds element
                even_odds_element.click()
                # Extract the value of the even odds
                even_odds_value = float(even_odds_element.text)
                # Print the value of the even odds
                print("Goal Even Odds Value:", even_odds_value)
                self.listOfAllOdds.append(even_odds_value)

    def get_odd_or_even_score(self, given_home_team, given_away_team, find):
        print(f"Looking for: {given_home_team} vs {given_away_team}")

        def filter_short_words(word_list):
            return [word for word in word_list if len(word) >= 3]

        con = 0
        tried = 0
        while True:
            con += 1
            # Quit the current driver
            global live_score_driver
            if tried >= 6:
                print(f"It couldn't find result after several trials of {given_home_team} vs {given_away_team}")
                return random.choice(["O", "E"])
            if con % 3 == 0:
                tried += 1
                self.live_score_driver.quit()
                # Create a new instance of the driver
                self.checking_browsers_are_open()
            elif con % 2:  # this will make it only refresh when it is finding the result of the match
                self.live_score_driver = live_score_driver
                self.live_score_driver.refresh()
            time.sleep(4)
            if con % 5 == 0:
                try:
                    # Wait until the dateBox element is present
                    date_box = WebDriverWait(live_score_driver, 10).until(
                        EC.presence_of_element_located((By.ID, "dateBox"))
                    )

                    # Get all option elements within the dateBox
                    options = date_box.find_elements(By.TAG_NAME, "option")

                    # Calculate yesterday's date
                    yesterday = datetime.now() - timedelta(days=1)
                    yesterday_str = yesterday.strftime('%Y-%m-%d')

                    # Iterate through the options to find and click the one corresponding to yesterday's date
                    for option in options:
                        if option.get_attribute("value") == yesterday_str:
                            option.click()
                            time.sleep(4)  # Wait for the page to reload with new date
                            break

                except Exception as e:
                    print(f"Exception occurred while changing the date: {e}")

            try:
                competition_tables = WebDriverWait(self.live_score_driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#allCont > div[id^='s0compTable']"))
                )
            except Exception as e:
                print(f"Exception occurred while waiting for competition tables: {e}")
                continue

            outer_break = False  # Flag to indicate if we need to break out of the outer loop
            if con > 5:
                print(f"competition_tables length: {len(competition_tables)}")
            numberOfError = 0
            for table in competition_tables:
                if numberOfError > 5:
                    time.sleep(7)
                    break
                try:
                    game_containers = WebDriverWait(table, 10).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[id^='s0gametr']"))
                    )
                except Exception as e:
                    numberOfError += 1
                    print(f"Exception occurred while waiting for game containers: {e}")
                    continue

                if con % 4 == 0 or con % 5 == 0:
                    print(f"game length: {len(game_containers)}")
                for container in game_containers:
                    try:
                        home_team = WebDriverWait(container, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, ".teamName.home"))
                        ).text
                        away_team = WebDriverWait(container, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, ".teamName.away"))
                        ).text
                        score_element = WebDriverWait(container, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, ".scoreOneRow b"))
                        )
                        score = score_element.text
                        start_time_element = WebDriverWait(container, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, ".time"))
                        )
                        start_time = start_time_element.text
                        match_status_element = WebDriverWait(container, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "[id^='sp0min']"))
                        )
                        match_status = match_status_element.text.strip()
                    except Exception as e:
                        print(f"Container Exception occurred: {e}")
                        continue

                    try:
                        home_team_list = filter_short_words(home_team.split())
                        away_team_list = filter_short_words(away_team.split())
                        given_home_team_list = filter_short_words(given_home_team.split())
                        given_away_team_list = filter_short_words(given_away_team.split())

                        if con % 4 == 0 or con % 5 == 0:
                            print(
                                f"{home_team_list} compare {given_home_team_list}   and  {away_team_list} compare {given_away_team_list} : {start_time} = ={self.find_match_time} == {self.match_starting_time}")

                        timeIs = False
                        if start_time == self.find_match_time or start_time == self.match_starting_time or tried >= 4:
                            timeIs = True

                        if ((set(home_team_list).intersection(given_home_team_list) and
                             set(away_team_list).intersection(given_away_team_list)) or
                            (set(home_team_list).intersection(given_home_team_list) and
                             set(home_team_list).intersection(
                                 given_away_team_list))) and timeIs:

                            print(f"Found: {home_team_list} vs {away_team_list}")
                            if (match_status == "Pst" or match_status == "-") and find:
                                print("Match has been postponed")
                                return "Not Found"
                            elif find:
                                return "Found"

                            print(f"Match Status: {match_status}")
                            if match_status in ["FT", "Pen", "ET", "AW", "AET"]:
                                try:
                                    home_score, away_score = map(int, score.split(" : "))
                                    total_score = home_score + away_score
                                    print("result completed")
                                    if match_status == "AET":
                                        return "E"
                                    return "O" if total_score % 2 != 0 else "E"
                                except:
                                    print("Match has no result after betting")
                                    return "Pst"
                            elif match_status == "Pst" or match_status == "Ssp":
                                print("Match was Postponed/Suspended after betting")
                                return "Pst"
                            elif match_status == "-" or match_status == "" or match_status == "'":
                                return "Repeat"

                            outer_break = True
                    except Exception as e:
                        print(f"Exception occurred in here: {e}")
                        continue

                if outer_break:
                    break  # Break out of the outer loop
            if find:
                print("Not Found")
                return "Not Found"
            print("200 seconds")
            time.sleep(200)

    def has_won(self, counting):
        with won_lock:
            inter = 0
            while True:
                try:
                    print(f"finding result for: {self.listOfAllMatchName[-1][0]} vs {self.listOfAllMatchName[-1][1]}")
                    result = self.get_odd_or_even_score(self.listOfAllMatchName[-1][0], self.listOfAllMatchName[-1][1],
                                                        False)
                    break
                except Exception as e:
                    print(f"Exception occurred: {e}")
                    print("Sleeping 3 seconds to refind result")
                    inter += 1
                    if inter > 2:
                        result = random.choice(["O", "E"])
                        print(f"result was not found and a random result was chosen as {result}")
                        break
                    time.sleep(3)

        with login_lock:
            self.login()
            time.sleep(2)
            self.handle_upcoming_tab()

        self.match_starting_time = None
        if result == self.betting_odd_even:
            self.ListOfAllWinMatch.append(self.listOfAllMatch[-1])
            print("Won the match")
            return True
        elif result == "Pst":
            self.match_PST = True
            return False
        elif result == "Repeat":
            print("Live score hasn't showed result, checking later")
            counting += 1
            if counting >= 3:
                self.match_PST = True
                return False
            time.sleep(7200)
            self.has_won(counting)
        elif result != "No result":
            print("Lost the match")
            self.listOfAllLostMatch.append(self.listOfAllMatch[-1])
            return False

    def pick_a_match(self):
        self.click_cancel_buttons(0)
        global listOfNotFoundMatchIndex
        sample_size = 3
        # Define Lagos timezone
        lagos_timezone = pytz.timezone('Africa/Lagos')

        # Create a while loop to repeat the process
        first_match_time = 0  # not needed but just to make a variable
        match_elements = []
        while True:
            try:
                # Wait for the table to load
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'sports-table__time')))
                # Find all match info elements
                match_elements = self.driver.find_elements(By.CSS_SELECTOR,
                                                           '.sports-table .table-f')  # Adjusted CSS selector
            except:
                print("pick a match error 2 sleeping for 120 seconds")
                time.sleep(120)
                self.login()
                self.handle_popups()
                self.handle_upcoming_tab()
                time.sleep(3)
                continue

            # Get current time in Lagos
            lagos_time_now = datetime.now(lagos_timezone)
            # Extract only the time part
            lagos_time_only = lagos_time_now.time()

            # Convert the time to seconds after midnight
            seconds_after_midnight = lagos_time_only.hour * 3600 + lagos_time_only.minute * 60 + lagos_time_only.second

            # so that it doesn't pick any match that before it makes the bet the match will have started
            # If there are match elements
            if len(match_elements) != 0:
                # Get the text of the first match element
                first_match_time = match_elements[0].text.split()[0]

                # Parse the first match time string to a datetime object
                first_match_time_real = datetime.strptime(first_match_time, '%H:%M')

                # Extract only the time part
                first_match_time_only = first_match_time_real.time()

                # Convert the time to seconds after midnight
                first_match_seconds_after_midnight = first_match_time_only.hour * 3600 + first_match_time_only.minute * 60 + first_match_time_only.second

                # Check if the first match starts in less than 4 minutes
                if abs(first_match_seconds_after_midnight - seconds_after_midnight) < 240:
                    print("sleeping to pick another match instead: wait for 100 seconds")
                    listOfNotFoundMatchIndex = []
                    time.sleep(100)
                    self.login()
                    time.sleep(3)
                    self.handle_popups()
                    self.handle_upcoming_tab()
                    continue  # Continue to the next iteration of the while loop

            # If no match elements or the first match is not within 4 minutes, break out of the loop
            break

        my_match = []
        plus = 0
        if len(match_elements) >= sample_size:  # you can use != 0 for a case of just 1 thread
            for index, match in enumerate(match_elements):
                if index >= sample_size + plus:  # Break the loop after the first three matches
                    break
                try:
                    timetime = match.text.split()[0]
                    self.match_starting_time = self.find_match_time = timetime  # Assuming the time is the first part of the match text
                except Exception as e:
                    continue  # break
                lagos_tz = pytz.timezone('Africa/Lagos')
                current_time = datetime.now(lagos_tz)
                # Get the current date and time
                current_year = current_time.year
                current_month = current_time.month
                current_day = current_time.day

                # Construct the datetime object for the match time
                match_datetime_str = f"{current_day} {current_month} {current_year} {self.match_starting_time}"
                match_datetime_naive = datetime.strptime(match_datetime_str, "%d %m %Y %H:%M")

                # Make match datetime offset-aware
                match_datetime = lagos_tz.localize(match_datetime_naive)

                # If match time is before current time, adjust to next day
                if match_datetime < current_time:
                    match_datetime += timedelta(days=1)

                # Calculate sleep duration
                sleep_duration = (match_datetime - current_time).total_seconds()
                try:
                    """" (self.find_match_time == first_match_time) and """
                    if index not in listOfNotFoundMatchIndex and sleep_duration < 6000:
                        if (self.get_odd_or_even_score(match.text.splitlines()[1], match.text.splitlines()[2],
                                                       True) == "Found"):
                            my_match.append(match)
                        else:
                            print("not here")
                            listOfNotFoundMatchIndex.append(index)
                            print(
                                f"{match.text.splitlines()[1]} vs {match.text.splitlines()[2]} ADDED TO list of not found")
                            plus += 1
                    else:
                        plus += 1
                        if sleep_duration >= 6000:
                            break

                except Exception as e:
                    print(f"Exception {e}")
                    print("Error while finding match, sleeping for 3 seconds")
                    time.sleep(3)

            if len(my_match) < sample_size:
                print("Sample size was less than 3, resetting list")
                listOfNotFoundMatchIndex = []  # Just because some match can get pst and remove which ruin the index

            if len(my_match) == 0:
                print("Length is equal zero")
                print("sleeping for 120 seconds since length is zero")
                time.sleep(120)
                self.login()
                self.handle_popups()
                self.handle_upcoming_tab()
                self.pick_a_match()
            else:
                try:
                    print("myMatch size: ", len(my_match))
                    match_to_bet = random.choice(my_match)

                    # Construct the datetime object for the match time
                    lagos_tz = pytz.timezone('Africa/Lagos')
                    current_time = datetime.now(lagos_tz)
                    # Get the current date and time
                    self.match_starting_time = match_to_bet.text.split()[0]
                    current_year = current_time.year
                    current_month = current_time.month
                    current_day = current_time.day
                    match_datetime_str = f"{current_day} {current_month} {current_year} {self.match_starting_time}"
                    match_datetime_naive = datetime.strptime(match_datetime_str, "%d %m %Y %H:%M")

                    # Make match datetime offset-aware
                    match_datetime = lagos_tz.localize(match_datetime_naive)

                    # If match time is before current time, adjust to next day
                    if match_datetime < current_time:
                        match_datetime += timedelta(days=1)

                    match_to_bet_text_rows = match_to_bet.text.splitlines()  # Split the text into rows
                    try:
                        self.listOfAllMatch.append(match_to_bet)
                        match_to_bet.click()
                        time.sleep(4)
                        self.dataForEachMatch()

                        print(f"player team: {match_to_bet_text_rows[1]} vs {match_to_bet_text_rows[2]}")
                        self.listOfAllMatchName.append((match_to_bet_text_rows[1], match_to_bet_text_rows[2]))
                        print("time: ", self.match_starting_time)

                        self.sleep_duration = timedelta(
                            seconds=(match_datetime - datetime.now(lagos_tz)).total_seconds())
                    except:
                        self.login()
                        self.driver.get("https://sports.bet9ja.com/sport/soccer/1")
                        self.handle_popups()
                        self.handle_upcoming_tab()
                        self.pick_a_match()
                except:
                    print("pick a match error 1 sleeping for 120 seconds")
                    time.sleep(120)
                    self.login()
                    self.handle_popups()
                    self.handle_upcoming_tab()
                    self.pick_a_match()

        else:
            print("pick a match error 2 sleeping for 120 seconds")
            time.sleep(120)
            self.login()
            self.handle_popups()
            self.handle_upcoming_tab()
            self.pick_a_match()

    def calculate_next_stakes(self, odd, trial):
        global shareDistribution, globalCount, globalDividedNumber
        next_stake = int(
            (np.sum(self.listOfAllAmountPlaced) + (
                    self.starting_stake * (odd - 1) * (len(self.listOfAllAmountPlaced) + 1))) / (odd - 1))
        if shareDistribution is not None and trial >= 3:
            if globalCount < globalDividedNumber:
                globalCount += 1
                next_stake = int(next_stake + shareDistribution)
            else:
                globalCount = 0
                shareDistribution = None
        next_stake += random.randint(0, 30)  # this is to prevent exactly
        # the same amount for each bet, so that it can correctly check if the bet was placed successfully
        self.listOfAllAmountPlaced.append(next_stake)
        return next_stake

    def handle_popups(self):
        try:
            # Wait for the button to be clickable
            button = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'novasdk-inbox-app-widget__close'))
            )

            # Click the button
            button.click()
        except:
            print("No popups to handle")

    def login(self):
        try:
            # Handle popups if present
            self.handle_popups()
            login_button = WebDriverWait(self.driver, 4).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-primary-m.btn-login'))
            )
            login_button.click()
            # Find and fill in the username field
            self.fill_input_field(By.ID, "username", self.username)
            # Find and fill in the password field
            self.fill_input_field(By.ID, "password", self.password)
            # Click on the login button
            login_button = WebDriverWait(self.driver, 4).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-primary-l.mt20'))
            )
            login_button.click()
            time.sleep(3)
            self.driver.refresh()
            print('Login successful')
            return True
        except Exception as e:
            print(f'An error occurred during login:')
            self.driver.refresh()
            time.sleep(5)
            # this is for a case where refresh is need to show login

            try:
                # Handle popups if present
                self.handle_popups()
                login_button = WebDriverWait(self.driver, 4).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-primary-m.btn-login'))
                )
                login_button.click()
                # Find and fill in the username field
                self.fill_input_field(By.ID, "username", self.username)
                # Find and fill in the password field
                self.fill_input_field(By.ID, "password", self.password)
                # Click on the login button
                login_button = WebDriverWait(self.driver, 4).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-primary-l.mt20'))
                )
                login_button.click()
                time.sleep(3)
                self.driver.refresh()
                print('Login successful')
                return True
            except Exception as e:
                print(f'An error occurred during login:')
            return False

    def handle_upcoming_tab(self):
        time.sleep(5)
        while True:
            try:
                # Find and click on the "Upcoming" tab
                upcoming_tab = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//li[contains(text(), "Upcoming")]'))
                )
                upcoming_tab.click()
                time.sleep(2)
                if self.betType == "Goal":
                    odd_even_tab = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//td[contains(text(), "Odd/Even")]'))
                    )
                    odd_even_tab.click()
                time.sleep(6)
                break
            except Exception as e:
                print(f"An error occurred while handling the upcoming tab: {e}")
                self.driver.get("https://sports.bet9ja.com/sport/soccer/1")
                time.sleep(100)
                try:
                    self.handle_popups()
                    if not self.login():
                        print("Login failed, retrying...")
                        continue
                    else:
                        print("Login successful")
                except:
                    print("Failed to handle popups or login")
                    continue

    def calculate_estimated_profit_and_risk(self):
        estimated_risk = (1 / (2 ** self.number_of_trials))
        number_of_trials_per_day = 5
        min_amount_needed = self.total_account_balance_needed()
        if self.amount_to_use < min_amount_needed:
            self.amount_to_use = min_amount_needed
        estimated_return = (1 + ((self.stake_distribution_starting_stake() * (
                self.average_odd - 1) * number_of_trials_per_day * self.num_bet_per_hour()) / self.amount_to_use)) ** 30 * self.amount_to_use
        return estimated_return, estimated_risk

    def place_bet(self, next_stake):
        if self.get_account_balance() <= next_stake:
            self.click_cancel_buttons(0)
            print('Failed to place bet because account balance is lesser than stake')
            return False
        try:
            if self.betTimes == 0:
                try:
                    # Wait for the Clear button to be clickable
                    clear_button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.CLASS_NAME, "basket-preset-values__item"))
                    )
                    clear_button.click()

                    # Locate the input element for stake
                    stake_input = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, ".input__holder .input"))
                    )

                    # Input the desired stake amount
                    stake_input.send_keys(str(next_stake))

                    # Click on the "Place Bet" button
                    place_bet_button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.ID, "betslip_buttons_placebet"))
                    )

                    place_bet_button.click()

                    # Wait for the "Continue" button to be clickable
                    continue_button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.CLASS_NAME, "btn-betslip-s"))
                    )

                    # Click on the "Continue" button
                    continue_button.click()
                except:
                    print("something went wrong, maybe betBOOM")
            print("10 seconds sleep")
            time.sleep(10)
            found = 0
            while True:
                self.driver.get('https://sports.bet9ja.com/myBets/')
                try:
                    # Wait for all accordion items to load
                    accordion_items = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_all_elements_located((By.XPATH, '//div[@class="accordion-item mt10"]'))
                    )
                    break
                except:
                    found += 1
                    if found > 3:
                        break
                    continue

            print("len: ", len(accordion_items))
            # Extract the stake amount using regex
            stake_element = accordion_items[0].find_element(By.XPATH, ".//div[contains(text(), 'Stake')]")
            stake_text = stake_element.text.strip()
            stake_amount = re.search(r'[\d,]+\.\d{2}', stake_text)
            outcome_text = float(stake_amount.group().replace(',', ''))
            print(f"Open Bet stake : {outcome_text}    next stake : {next_stake}")
            # Get the team names
            team_element = accordion_items[0].find_element(By.XPATH, './/div[@class="mybets-bet txt-cut"]')
            team_name = team_element.text.strip()
            # Split team_name into two parts
            teams = team_name.split(" - ")
            # Get the last match names tuple
            print(f"Team: {team_name}   listName:  {self.listOfAllMatchName[-1]}")
            # Properly compare team names
            if teams != list(self.listOfAllMatchName[-1]) or float(outcome_text) != float(next_stake):
                print("The bet was void")
                print("rechecking again")
                time.sleep(5)
                self.betTimes += 1
                if self.betTimes >= 3:
                    self.betTimes = 0
                    print("The bet was void after rechecking again")
                    return False
                self.driver.refresh()
                return self.place_bet(next_stake)

            return True
        except Exception as e:
            self.click_cancel_buttons(0)
            print('Failed to place bet')
            return False

    def checking_browsers_are_open(self):
        global driver, live_score_driver
        while True:
            print("checking bet9ja browser is still open")
            try:
                # Attempt to access the driver to check if it is still open
                current_url = driver.current_url
                print(f"Browser is open. Current URL: {current_url}")
                break
            except:
                # If accessing the driver fails, it means the browser is closed
                print("Browser closed. Reopening...")
                driver = webdriver.Chrome()
                # Set the size of the windows
                driver.set_window_size(1000, 800)
                driver.set_window_position(540, 0)
                driver.get("https://sports.bet9ja.com/sport/soccer/1")
                self.login()
                self.handle_popups()
                self.handle_upcoming_tab()

        while True:
            print("checking livescore browser is still open")
            try:
                # Attempt to access the driver to check if it is still open
                current_url = live_score_driver.current_url
                print(f"Browser is open. Current URL: {current_url}")
                break
            except:
                # If accessing the driver fails, it means the browser is closed
                print("Browser closed. Reopening...")
                live_score_driver = webdriver.Chrome()
                # Set the size of the windows
                live_score_driver.set_window_size(400, 800)
                live_score_driver.set_window_position(0, 0)
                live_score_driver.get("http://www.goals365.com/feed/soccer/")
        self.driver = driver
        self.live_score_driver = live_score_driver

    def bet_num_games_with_trials(self):
        global shareDistribution, globalDividedNumber, sum_of_all_profit_made
        time.sleep(20)  # Just so that all other thread will wait for the main thread to login
        ############################################################
        amount_to_use = self.amount_to_use
        counting_fail_trials = random.randint(0, 2)
        counting_fail_trials = 0
        # for i in range(counting_fail_trials):
        #     if i == 0:
        #         self.listOfAllAmountPlaced.append(self.stake_distribution_starting_stake())
        #     else:
        #         self.listOfAllOdds.append(1.85)
        #         self.calculate_next_stakes(self.listOfAllOdds[-1], i)

        ######################################################################
        print(f"counting_fail_trials: {counting_fail_trials}   self: {self.listOfAllAmountPlaced}")

        total_failed_trials = 0
        listOfAllTotalFailedTrials = []
        original_number_of_trials = self.number_of_trials

        while True:
            self.checking_browsers_are_open()
            self.starting_stake = self.stake_distribution_starting_stake()

            if counting_fail_trials == self.number_of_trials - 1:
                print("Trying to cover lost through Plan A")
                self.number_of_trials -= 1
                if self.number_of_trials <= (original_number_of_trials / 2) + 1:
                    print(
                        "You have lost a lot of money, you need to deposit and start over again to increase your chance of winning")
                    break

                self.amount_to_use = self.amount_to_use - np.sum(self.listOfAllAmountPlaced)
                self.starting_stake = self.stake_distribution_starting_stake()
                print(f"The total failed trial is: {total_failed_trials}")
                counting_fail_trials = 0
                self.listOfAllOdds = []
                self.listOfAllAmountPlaced = []
                self.listOfAllMatch = []
                self.listOfAllLostMatch = []
                self.listOfAllMatchName = []
                self.ListOfAllWinMatch = []
                print(f"starting stake: {self.starting_stake}  number of trials: {self.number_of_trials}")

            trial = counting_fail_trials

            while trial < self.number_of_trials - 1:
                with pick_a_match_lock:
                    time.sleep(50)  # very important sleep to make the previous thread finish betting. don't change
                    self.checking_browsers_are_open()
                    print(f"Number of threads: {threading.active_count()}")
                    global current_amount
                    self.thread_trails += 1
                    current_amount = self.get_account_balance()

                    try:
                        self.pick_a_match()
                    except:
                        print("This thread didn't pick a match successfully")
                        self.thread_trails -= 1
                        self.driver.get("https://sports.bet9ja.com/sport/soccer/1")
                        self.login()
                        self.handle_popups()
                        self.handle_upcoming_tab()
                        continue
                    print("finish waiting")
                print(f"current thread trials is {self.thread_trails}")

                with place_bet_lock:
                    print("ready to bet")
                    if trial == 0:
                        next_stake = self.starting_stake
                        self.listOfAllAmountPlaced.append(self.starting_stake)
                    elif trial != 0:
                        next_stake = self.calculate_next_stakes(self.listOfAllOdds[-1], trial)
                        print("trial is not zero")

                    bet = self.place_bet(next_stake)

                    if not bet:
                        try:
                            self.listOfAllAmountPlaced.pop()
                            self.listOfAllOdds.pop()
                        except:
                            print("Error popping")
                        print("It didn't bet so we popped from list of all amount")
                        continue
                    else:
                        print(f"Bet of {next_stake} has been placed successfully")

                    trial += 1
                    print(
                        f"Waiting till the match ends: match will end at {datetime.now() + self.sleep_duration + timedelta(seconds=6900)}")
                    print(f"The sleeping duration before match starts is: {self.sleep_duration.total_seconds()}")
                    print(f"The sleeping duration is: {self.sleep_duration.total_seconds() + 6900}")
                    self.driver.get("https://sports.bet9ja.com/sport/soccer/1")
                    self.login()
                    self.handle_popups()
                    self.handle_upcoming_tab()

                time.sleep(self.sleep_duration.total_seconds() + 6900)
                print("done sleeping")
                self.checking_browsers_are_open()
                counting = 0
                if self.has_won(counting):
                    # Get the number of threads
                    num_threads = threading.active_count()
                    print(f"Number of threads: {num_threads}")
                    print(f"number of Failed trials before winning is: {total_failed_trials}")
                    listOfAllTotalFailedTrials.append(total_failed_trials)
                    counting_fail_trials = 0
                    total_failed_trials = 0
                    current_gain = (self.listOfAllOdds[-1] * self.listOfAllAmountPlaced[-1]) - np.sum(
                        self.listOfAllAmountPlaced)
                    print(
                        f"current gain: {current_gain} = ({self.listOfAllOdds[-1]} * {self.listOfAllAmountPlaced[-1]}) - {np.sum(self.listOfAllAmountPlaced)}")
                    sum_of_all_profit_made += current_gain
                    print(f"Total Profit Made: {sum_of_all_profit_made}")
                    self.amount_to_use = amount_to_use + sum_of_all_profit_made - 10
                    self.number_of_trials += 1  # some important reason for this
                    if self.stake_distribution_starting_stake() >= 100 and self.number_of_trials - 1 < original_number_of_trials:
                        self.number_of_trials += 1
                    self.number_of_trials -= 1  # and this sets it back
                    self.listOfAllOdds = []
                    self.listOfAllAmountPlaced = []
                    self.listOfAllMatch = []
                    self.listOfAllLostMatch = []
                    self.listOfAllMatchName = []
                    self.ListOfAllWinMatch = []
                    if should_stop_event.is_set():
                        print("Stopping the current thread after winning the match.")
                        return
                    break
                else:

                    if self.match_PST:
                        print("done losing but it did not lose, it was postponed")
                        self.match_PST = False
                        counting_fail_trials -= 1
                        total_failed_trials -= 1
                        self.listOfAllOdds.pop()
                        self.listOfAllAmountPlaced.pop()
                        self.listOfAllMatchName.pop()
                        trial -= 1

                    print("done losing")
                    counting_fail_trials += 1
                    total_failed_trials += 1
                    print(f"number of Failed trials is: {total_failed_trials}")
                    num_threads = threading.active_count()
                    print(f"Number of threads: {num_threads}")

                    if trial >= self.number_of_trials - 1:
                        shareDistribution = int(sum(self.listOfAllAmountPlaced) / globalDividedNumber)
                        globalDividedNumber += globalDividedNumber
                        self.amount_to_use = amount_to_use + sum_of_all_profit_made - 10
                        print("Trying to cover lost through Plan B")
                        print("start again, No fucking profit")
                        break

            print(f"List of all failed trials before win: {listOfAllTotalFailedTrials}")

    def run(self):
        # Set the size of the windows
        self.driver.set_window_size(1000, 800)
        self.driver.set_window_position(540, 0)
        self.live_score_driver.set_window_size(400, 800)
        self.live_score_driver.set_window_position(0, 0)

        self.driver.get("https://sports.bet9ja.com/sport/soccer/1")
        self.live_score_driver.get("http://www.goals365.com/feed/soccer/")
        if not self.login():
            return
        self.handle_upcoming_tab()
        self.balance_clearance()


bet9ja_bot = Bet9jaBot(username, password, average_odd, amount_to_use, number_of_trials, starting_stake,
                       potential_monthly_Profit, betType, "O")
estimated_return, estimated_risk = bet9ja_bot.calculate_estimated_profit_and_risk()
print(f"minimum amount needed/ Deposit: {bet9ja_bot.total_account_balance_needed()}")
print(f"Number of trials : {number_of_trials}")
print(f"Number of bet per hour: {bet9ja_bot.num_bet_per_hour()}")
print(f"Estimated return: {estimated_return}")
print(f"Multiple return: {(estimated_return / bet9ja_bot.amount_to_use)}")
print(f"Estimated Profit: {estimated_return - bet9ja_bot.amount_to_use}")
print(f"Profit percentage: {((estimated_return - bet9ja_bot.amount_to_use) / bet9ja_bot.amount_to_use) * 100}%")
print(f"Estimated Risk: {estimated_risk}")
print(f"Winning probability: {1 - estimated_risk}    Lost rate: {bet9ja_bot.num_bet_per_hour() * estimated_risk}")

# Create and run the bot
listOfAllBetInstance = [
    Bet9jaBot(username, password, average_odd, amount_to_use, number_of_trials, starting_stake,
              potential_monthly_Profit, betType, "O")  # "E" if i % 2 == 0 else "O"
    for i in range(bet9ja_bot.num_bet_per_hour())  # bet9ja_bot.num_bet_per_hour()
]

# Create threads for all instances except the first one
threads = [threading.Thread(target=bot_instance.bet_num_games_with_trials, args=()) for bot_instance in
           listOfAllBetInstance]

# Start threads for all instances except the first one
for thread in threads:
    thread.start()

bet9ja_bot.run()
print(f"Number of threads: {threading.active_count()}")

# Wait for all threads to complete
for thread in threads:
    thread.join()
