import requests
import datetime as dt
import os

SHEETY_ENDPOINT = os.environ.get('SHEETY_FLIGHT_ENDPOINT')
prices_url = f"{SHEETY_ENDPOINT}/prices"
users_url = f"{SHEETY_ENDPOINT}/users"


class DataManager:

    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {os.environ.get('SHEETY_FLIGHT_TOKEN')}"
        }

    def get_data(self):
        response = requests.get(url=prices_url, headers=self.headers)
        return response.json()["prices"]

    def update_data(self, row_id, city_dict):
        new_data = {
            "price": {
                "iataCode": city_dict["iataCode"]
            }
        }
        response = requests.put(url=f"{prices_url}/{row_id}", json=new_data, headers=self.headers)

    def get_users(self):
        response = requests.get(url=users_url, headers=self.headers)
        return response.json()["users"]