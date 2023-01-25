import requests
import os
from twilio.rest import Client

account_sid = os.environ.get('TWILIO_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def price_alert(self, price, departure_city_name, departure_airport_code, arrival_city_name,
                    arrival_airport_code, outbound_date, inbound_date):
        message = self.client.messages.create(
            body=f"Low price alert! Only £{price} to fly from {departure_city_name}-{departure_airport_code} to {arrival_city_name}-{arrival_airport_code}, from {outbound_date} to {inbound_date}.",
            from_=os.environ.get('TWILIO_PHONE'),
            to=os.environ.get('MY_PHONE')
        )
        print(message.status)