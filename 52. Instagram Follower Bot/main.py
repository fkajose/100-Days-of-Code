# Import necessary modules from selenium library
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
import os
from time import sleep

# Path to Chrome driver
CHROME_DRIVER_PATH = "C:/Users/User/Documents/Development/chromedriver.exe"

SIMILAR_ACCOUNT = "cristiano"
USERNAME = os.environ.get("TEST_IG_ACC")
PASSWORD = os.environ.get("TEST_IG_PASSWORD")
IG_LOGIN_PAGE = "https://www.instagram.com/accounts/login/"


def __init__(self, driver_path):
    """A class to automate following Instagram followers of a given account.

    Attributes:
        driver_path (str): The file path to the Chrome driver.

    Methods:
        login(url, username, password): Logs into Instagram with the given username and password.
        find_followers(account): Navigates to the followers popup of the given account and scrolls through it.
        follow(): Follows all users listed in the followers popup.
    """

    self.service = Service(driver_path)
    self.driver = webdriver.Chrome(service=self.service)


def login(self, url, username, password):
    """
    Method to login to Instagram account

    Args:
    url (str): Instagram login page URL
    username (str): Instagram account username
    password (str): Instagram account password
    """
    self.driver.get(url)

    sleep(3)

    # Enter username
    username_field = self.driver.find_element(By.NAME, "username")
    username_field.send_keys(username)

    sleep(1)

    # Enter password
    password_field = self.driver.find_element(By.NAME, "password")
    password_field.send_keys(password)
    password_field.send_keys(Keys.ENTER)

    sleep(5)


def find_followers(self, account):
    """
    Method to find the followers of an Instagram account

    Args:
    account (str): Instagram account to find the followers of
    """
    url = f"https://www.instagram.com/{account}/followers/"
    self.driver.get(url)
    sleep(2)

    # Get the followers popup element
    followers_popup = self.driver.find_element(
        By.XPATH, '//*[@id="mount_0_0_qa"]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]')

    # Scroll the followers popup 20 times to load more followers
    for i in range(20):
        self.driver.execute_script(
            "arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)
        sleep(2)


def follow(self):
    """
    Method to follow all the followers of an Instagram account
    """
    all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
    for button in all_buttons:
        try:
            if button.text == "Follow":
                button.click()
                sleep(1)

        except ElementClickInterceptedException:
            # If the follow button is not clickable due to an interception,
            # click the cancel button to dismiss the popup
            cancel_button = self.driver.find_element_by_xpath(
                '/html/body/div[5]/div/div/div/div[3]/button[2]')
            cancel_button.click()

    # Scroll to the bottom of the page to load more followers
    self.driver.execute_script(
        "argument[0].scrollIntoView(true);", all_buttons[-1])


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login(IG_LOGIN_PAGE, USERNAME, PASSWORD)
bot.find_followers(SIMILAR_ACCOUNT)
bot.follow()
