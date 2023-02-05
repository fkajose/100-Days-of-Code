# Import necessary modules from selenium library
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from time import sleep

# Constants for the promised internet speed
PROMISED_DOWN = 150
PROMISED_UP = 10
# Path to Chrome driver
CHROME_DRIVER_PATH = "C:/Users/User/Documents/Development/chromedriver.exe"
# Email and password for Twitter account
TWITTER_EMAIL = os.environ.get("TEST_GMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_TEST_PWORD")

class InternetSpeedTwitterBot:
    """Class to perform automated speed test and tweet at the internet service provider

    Args:
        driver_path (str): Path to the Chrome Driver executable file.
    """
    def __init__(self, driver_path):
        """Initialize the class and set default values for up, down, and provider."""
        self.driver = webdriver.Chrome(driver_path)
        self.up = 0
        self.down = 0
        self.provider = ""
        
    def get_internet_speed(self, url="https://www.speedtest.net/"):
        """Perform the internet speed test and set the results for up and down.

        Args:
            url (str, optional): URL for the speed test website. Default is "https://www.speedtest.net/".
        """
        # Load the URL in the browser
        self.driver.get(url)

        sleep(5)
        
        # Get the internet service provider name
        self.provider = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[4]/div/div[2]/div/div[1]/div/div[2]').text
        
        # Find and click the "Go" button to start the speed test
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()

        # Wait for 60 seconds for the speed test to complete
        sleep(60)
        
        # Get the upload speed
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        # Get the download speed
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text

        # Print the results for debugging
        print(f"""up: {self.up},
                down: {self.down}
                provider: {self.provider}""")
        

    def tweet_at_provider(self, url="https://twitter.com/login"):
        """Perform automated login to Twitter, create a tweet and send it.

            Args:
                url (str, optional): URL for the Twitter login page. Default is "https://twitter.com/login".
            """
        # Load the Twitter login page
        self.driver.get(url)
        
        # Wait for the page to load
        sleep(5)
        
        # Enter the email address for Twitter login
        email = self.driver.find_element(By.NAME, "text")
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)

        # Wait for the password field to load
        sleep(5)
        
        # Enter the password for Twitter login
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        
        # Wait for the Twitter homepage to load
        sleep(5)

        # Generate the message to be tweeted, using the values of up, down and provider obtained from the previous method call
        msg = f"""Hey {self.provider}, why is my internet speed
            {self.down}down/{self.up}up?"""
        
        # Click the Tweet button to compose a new tweet
        self.driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Tweet"]').click()
        
        # Find the text box to enter the tweet
        tweet_box = self.driver.find_element(By.CSS_SELECTOR, 'div[data-contents="true"]')
        
        # Enter the tweet
        tweet_box.send_keys(msg)
        
        # Wait for the tweet button to become available
        sleep(5)
        
        # Click the tweet button to send the tweet
        self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetButton"]').click()
        
        # Wait for the tweet to post
        sleep(2)
        
        # Quit the webdriver
        self.driver.quit()
        


# Instantiate and use bot
bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
speed = bot.get_internet_speed()
bot.tweet_at_provider()
