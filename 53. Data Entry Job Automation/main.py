# Import necessary modules from selenium library
from selenium.webdriver.common.window import WindowTypes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep
import pandas
import numpy


form_url = 'https://forms.gle/m8AKi6pSwWVTXr3y5'
zillow_url = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'


# Path to the chromedriver executable
driver_path = "C:/Users/User/Documents/Development/chromedriver.exe"

# Start a new instance of the Chrome browser using chromedriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Open the Zillow search results page in the browser
driver.get(zillow_url)
sleep(2)

# Find all the link elements for the properties listed on the page
link_elements = driver.find_elements(By.CSS_SELECTOR, ".property-card-link")

# Extract the href attribute for each link element and store in a numpy array
links_with_duplicates = numpy.array(
    [link.get_attribute('href') for link in link_elements])

# Get the indices and sort to remove duplicates
indices = numpy.unique(links_with_duplicates, return_index=True)[1]
links = links_with_duplicates[numpy.sort(indices)]

# Create a list of prices for all the listings scraped.
price_elements = driver.find_elements(
    By.CSS_SELECTOR, "span[data-test='property-card-price']")
prices = [price.text for price in price_elements]

# Create a list of addresses for all the listings scraped.
address_elements = driver.find_elements(
    By.CSS_SELECTOR, "address")
addresses = [address.text for address in address_elements]

# Store data
data = pandas.DataFrame({
    "address": addresses,
    "price": prices,
    "link": links
})

data.to_csv("53. Data Entry Job Automation/zillow_house_data.csv")


def fill_form(row):
    """
    Fills out and submits a Google Form with the data in the given row.

    Args:
    row: A pandas Series containing data for a single row of the form. Must have the following columns:
         - address: A string containing the address of the property.
         - price: A string containing the price of the property.
         - link: A string containing the URL of the property listing.

    Returns:
    None
    """

    # Load form and wait for it to load
    driver.get(form_url)
    sleep(2)

    # Find the input fields on the form
    input_fields = driver.find_elements(By.CSS_SELECTOR, "input[type=text]")
    addr_field, price_field, link_field = input_fields[0], input_fields[1], input_fields[2]

    # Fill in the input fields with the data from the row
    addr_field.send_keys(row["address"])
    price_field.send_keys(row["price"])
    link_field.send_keys(row["link"])

    # Find the submit button and click it
    submit_button = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()


# Open new tab
driver.switch_to.new_window(WindowTypes.TAB)

# Fill form with function
data.apply(fill_form, axis=1)

driver.quit()
