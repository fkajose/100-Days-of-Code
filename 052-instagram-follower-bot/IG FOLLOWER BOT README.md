# Instagram Follower Bot

This program is designed to automate the process of following all the followers of a given Instagram account. It uses Selenium, a popular tool for automating web browsers, to navigate Instagram's web interface and perform the necessary actions.

## Installation

Before using this program, you need to install Selenium and the Chrome driver. You can install Selenium using pip:

```python
pip install selenium
```

You also need to download the Chrome driver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in a directory on your computer. Make sure to specify the path to the Chrome driver when initializing the InstaFollower class.

## Usage

To use the bot, create an instance of the InstaFollower class and call the login, find_followers, and follow methods in order.

```python
from InstaFollower import InstaFollower

CHROME_DRIVER_PATH = "C:/Users/User/Documents/Development/chromedriver.exe"
SIMILAR_ACCOUNT = "cristiano"
USERNAME = "your_instagram_username"
PASSWORD = "your_instagram_password"
IG_LOGIN_PAGE = "https://www.instagram.com/accounts/login/"

bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login(IG_LOGIN_PAGE, USERNAME, PASSWORD)
bot.find_followers(SIMILAR_ACCOUNT)
bot.follow()
```

The login method logs into your Instagram account with the given username and password. The find_followers method navigates to the followers popup of the given account and scrolls through it to load all followers. The follow method follows all users listed in the followers popup.

**Note:** that the program is designed to follow all users listed in the popup, so use it at your own risk. Following too many accounts in a short amount of time may result in your account being flagged as spam and potentially being suspended or banned. Instagram also limits the number of accounts you can follow at once.
