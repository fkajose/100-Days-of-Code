# Import necessary modules from selenium library
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import os
import time

# Load environment variables for LinkedIn email and password
USERNAME = os.environ.get('TEST_GMAIL')
PASSWORD = os.environ.get('FB_TEST_PASSWORD')

# Path to the chrome driver executable
chrome_driver_path = "C:/Users/User/Documents/Development/chromedriver.exe"

# Initialize a chrome driver object
driver = webdriver.Chrome(chrome_driver_path)

url = "https://tinder.com/app/recs"
driver.get(url)

sign_in = driver.find_element(By.CLASS_NAME, "w1u9t036")
sign_in.click()
time.sleep(2)

# Select Facebook option
facebook = driver.find_element(By.CSS_SELECTOR, "button c1p6lbu0")
facebook.click()
time.sleep(2)

# Switch to Facebook window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# Inout Facebook info
email_address = driver.find_element(By.ID, "m_login_email")
password = driver.find_element(By.ID, "m_login_password")
email_address.send_keys(USERNAME)
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(5)

driver.switch_to.window(base_window)
print(driver.title)

#Delay by 5 seconds to allow page to load.
time.sleep(5)

#Allow location
allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

#Disallow notifications
notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

#Allow cookies
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add a 1 second delay between likes.
    time.sleep(1)

    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
