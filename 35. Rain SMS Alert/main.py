import requests, datetime as dt
from twilio.rest import Client
import os

MY_LAT = 6.416970
MY_LONG = 2.883430
api_key = os.environ.get('OPENWEATHER_API_KEY')

account_sid = os.environ.get('TWILIO_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

current_hour = dt.datetime.now().hour

weather_data = response.json()["hourly"]
sliced_weather_data = [
    hour["weather"][0]['id'] for hour in weather_data[current_hour:current_hour + 13] if hour["weather"][0]['id'] < 700
]
print(sliced_weather_data)
if sliced_weather_data:
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella. ☔",
        from_=os.environ.get('TWILIO_PHONE'),
        to=os.environ.get('MY_PHONE')
    )

    print(message.status)
