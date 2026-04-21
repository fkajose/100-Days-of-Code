#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime as dt

ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_data()
user_data = data_manager.get_users()
pprint(user_data)

today = dt.datetime.now()
tomorrow = today + dt.timedelta(days=1)
six_months = today + dt.timedelta(days=180)

for destination in sheet_data:
    if destination["iataCode"] == "":
        city = destination["city"]
        destination["iataCode"] = flight_search.get_code(city)
        data_manager.update_data(row_id=destination["id"], city_dict=destination)

    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months
    )

    if flight is None:
        continue

    if flight.price <= destination["lowestPrice"]:
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        users = data_manager.get_users()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)
        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
        notification_manager.send_emails(emails, message, link)




