import smtplib
import requests
import os
from twilio.rest import Client

account_sid = os.environ.get('TWILIO_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

MY_EMAIL = os.environ.get('TEST_GMAIL')
MY_PASSWORD = os.environ.get('TEST_GMAIL_PASSWORD')


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, msg):
        message = self.client.messages.create(
            body=msg,
            from_=os.environ.get('TWILIO_PHONE'),
            to=os.environ.get('MY_PHONE')
        )
        print(message.status)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
