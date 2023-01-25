import requests
import datetime as dt
import os

SHEETY_ENDPOINT = os.environ.get('SHEETY_FLIGHT_ENDPOINT')


class DataManager:

    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # self.data_dict = {
        #     "price":
        #
        # }
        self.headers = {
            "Authorization": f"Bearer {os.environ.get('SHEETY_FLIGHT_TOKEN')}"
        }

    def get_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=self.headers)
        return response.json()["prices"]

    def update_data(self, row_id, city_dict):
        new_data = {
            "price": {
                "iataCode": city_dict["iataCode"]
            }
        }
        response = requests.put(url=f"{SHEETY_ENDPOINT}/{row_id}", json=new_data, headers=self.headers)
