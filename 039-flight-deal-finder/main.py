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

today = dt.datetime.now()
tomorrow = today + dt.timedelta(days=1)
six_months = today + dt.timedelta(days=180)

for data in sheet_data:
    if data["iataCode"] == "":
        city = data["city"]
        data["iataCode"] = flight_search.get_code(city)
        data_manager.update_data(row_id=data["id"], city_dict=data)

    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        data["iataCode"],
        from_time=tomorrow,
        to_time=six_months
    )

    if flight.price <= data["lowestPrice"]:
        notification_manager.price_alert(
            price=flight.price,
            departure_city_name="LONDON",
            departure_airport_code=ORIGIN_CITY_IATA,
            arrival_city_name=data["city"],
            arrival_airport_code=data["iataCode"],
            outbound_date=flight.out_date,
            inbound_date=flight.return_date
        )

