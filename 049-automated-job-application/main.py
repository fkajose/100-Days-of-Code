# Import necessary modules from selenium library
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
import time

# Load environment variables for LinkedIn email and password
USERNAME = os.environ.get('LINKEDIN_EMAIL')
PASSWORD = os.environ.get('LINKEDIN_PASSWORD')
PHONE = os.environ.get("MY_PHONE").replace("+234", "0")

# Path to the chrome driver executable
chrome_driver_path = "C:/Users/User/Documents/Development/chromedriver.exe"

# Initialize a chrome driver object
driver = webdriver.Chrome(chrome_driver_path)

# Load the target LinkedIn job search page
url = 'https://www.linkedin.com/jobs/search/?currentJobId=3434791641&f_AL=true&f_JT=F%2CP%2CI&f_WT=1%2C3%2C2&geoId=104197452&keywords=python%20developer&location=Lagos%20State%2C%20Nigeria&refresh=true'
driver.get(url)

# Click the sign in button to log in to LinkedIn
sign_in = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()

# Enter the LinkedIn email and password
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)

# Find all the job listings on the page and loop through them
all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    
    try:
        # Try to click the apply button on the job listing page
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()

        # If the phone field is empty, fill it with the user's phone number
        phone_field = driver.find_element(By.CLASS_NAME, "artdeco-text-input--input")
        if phone_field.text == "":
            phone_field.send_keys(PHONE)

        # If the submit button says something other than "Submit", the application is complex
        # In that case, skip the application
        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        
        if submit_button.text != "Submit":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            
            discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            time.sleep(2)
            print("Complex Application, Skipped!")
            continue
        else:
            submit_button.click()
            print("Applied for job!")
        
        #Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()
    
     #If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

        
time.sleep(10)
driver.quit()