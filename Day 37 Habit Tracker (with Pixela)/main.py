import os

import requests
import datetime as dt
import os

USERNAME = os.environ.get('PIXELA_USERNAME')
TOKEN = os.environ.get('PIXELA_TOKEN')

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph02",
    "name": "100 Days of Code Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = dt.datetime.now()

pixel_post_endpoint = f"{graph_endpoint}/graph02"

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you spend coding?\n"),
}

response = requests.post(url=pixel_post_endpoint, json=pixel_config, headers=headers)
print(response.text)

# pixel_update_endpoint = f"{graph_endpoint}/graph02/{today.strftime('%Y%m%d')}"
#
# update_data = {
#     "quantity": "1.5",
# }

# response = requests.put(url=pixel_update_endpoint, json=update_data, headers=headers)
# print(response.text)

# response = requests.delete(url=pixel_update_endpoint, headers=headers)
# print(response.text)
