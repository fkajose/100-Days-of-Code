import requests
from datetime import datetime
import time
import os

MY_LAT = 6.524379  # Your latitude
MY_LONG = 3.379206  # Your longitude

MY_EMAIL = os.environ.get('TEST_GMAIL')
MY_PASSWORD = os.environ.get('TEST_GMAIL_PASSWORD')

while True:
    time.sleep(60)
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    # If the ISS is close to my current position
    if MY_LAT - iss_latitude == abs(5) or MY_LONG - iss_longitude == abs(5):
        # and it is currently dark
        if time_now.hour >= sunset or time_now.hour <= sunrise:
            # Then send me an email to tell me to look up.
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg=f"Subject:Look Up!\n\nDon't miss the ISS. It's right overhead."
                )
# BONUS: run the code every 60 seconds.

