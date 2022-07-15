import requests

parameters = {
    "amount": 15,
    "type": "boolean",
    "difficulty": "easy",
    "category": 10
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

question_data = response.json()["results"]
