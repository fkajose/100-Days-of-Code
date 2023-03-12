# House Hunter

This is a Python script that uses Selenium to scrape rental listings from Zillow and automate filling out a Google Form with the data collected.

## Dependencies

This script requires the following dependencies:

- Python 3
- Selenium
- Pandas
- Numpy
- Google Chrome

## Usage

1. Clone the repository to your local machine.
2. Install the dependencies by running pip install -r requirements.txt.
3. Set the values of the form_url and zillow_url variables at the beginning of the script to the URLs of the Google Form and Zillow search results page, respectively.
4. Set the value of the driver_path variable to the path of the chromedriver executable on your machine.
5. Run the script using python house_hunter.py.
6. The script will scrape rental listings from the Zillow search results page, remove duplicates, and save the data to a CSV file. It will then open a new tab in Google Chrome and fill out and submit the Google Form with the data collected.

Note that the script has a sleep time of 2 seconds after loading each page. You may need to adjust this value depending on the speed of your internet connection.
