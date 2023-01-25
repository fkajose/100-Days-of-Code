import requests
import datetime as dt
import os

APP_ID = os.environ.get('NUTRITIONIX_APP_ID')
APP_KEY = os.environ.get('NUTRITIONIX_APP_KEY')
endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
TOKEN = os.environ.get('SHEETY_TOKEN')

exercise = input("Tell me which exercise you did: ")

data = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 60,
    "height_cm": 180,
    "age": 21,
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

response = requests.post(url=endpoint, json=data, headers=headers)
result = response.json()

now = dt.datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%X")

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

print(result)

for exercise in result["exercises"]:
    data_dict = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_endpoint = os.environ.get('SHEETY_WORKOUT_ENDPOINT')
    response = requests.post(url=sheety_endpoint, json=data_dict, headers=headers)
    print(response.text)