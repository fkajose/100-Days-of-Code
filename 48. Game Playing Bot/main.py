from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta

# URL of the cookie clicker game
url = "http://orteil.dashnet.org/experiments/cookie/"

# path to the chrome driver executable
chrome_driver_path = "C:/Users/User/Documents/Development/chromedriver.exe"

# Initialize a chrome driver
driver = webdriver.Chrome(chrome_driver_path)

# Navigate to the game URL
driver.get(url)

# Find the cookie element and click it
cookie = driver.find_element(By.ID, "cookie")

def get_price(upgrade):
        """
        Extracts the price of the given upgrade.

        Args:
            upgrade (WebElement): The WebElement of the upgrade.

        Returns:
            price (int): The price of the upgrade.
        """
        try:
            price = int(upgrade.text.split("-")[1].split("\n")[0].replace(",", ""))
            return price
        except:
            return None

def highest_upgrade(store):
    """
    Finds the highest priced upgrade that is currently available to purchase.

    Args:
        store (list): List of WebElements representing the upgrades in the store.

    Returns:
        highest_upgrade (WebElement): The WebElement of the highest upgrade available.
    """
    available_upgrades  = [item for item in store if (item.get_attribute("class") != "grayed") and (get_price(item))]
    max_upgrade_availabe = max([get_price(item) for item in available_upgrades])
    highest_upgrade = next(filter(
        lambda item: get_price(item) == max_upgrade_availabe, available_upgrades))

    return highest_upgrade

# Set the end time for the script to run
end_time = datetime.now() + timedelta(minutes=5)

# Set the time to check for upgrades
upgrade_timeout = datetime.now() + timedelta(seconds=5)

# Counter for the number of cookies clicked
cookie_count = 0

# Main loop
while True:
    # Click the cookie
    cookie.click()
    cookie_count += 1

    # Check if it's time to check for upgrades
    if datetime.now() >= upgrade_timeout:
        # Find the list of upgrades in the store
        store = driver.find_elements(By.CSS_SELECTOR, '#store div')
        # Find the highest priced upgrade that is currently available to purchase
        upgrade = highest_upgrade(store)

        # Check if we have enough cookies to purchase the upgrade
        if cookie_count >= get_price(upgrade):
            # Purchase the upgrade
            upgrade.click()

        # Update the upgrade check time
        upgrade_timeout += timedelta(seconds=5)

    # Check if it's time to end the script        
    if datetime.now() >= end_time:
        cookies_per_sec = driver.find_element(By.ID, "cps").text
        print(f"Done! {cookie_count} cookies baked. {cookies_per_sec}")
        break

driver.quit()