import json


def read_arguments_from_file(file_path):
    with open(file_path, "r") as f:
        arguments = []
        for line in f:
            line = line.strip()
            arguments.append(line.split(","))

    return arguments


def extract_flight_data(string):
    flights = json.loads(string)["best_departing_flights"]
    more_flights = json.loads(string)["other_departing_flights"]
    flights += more_flights
    flight_objects = []
    for flight in flights:
        flight_object = {
            "departure_date": flight["departure_date"],
            "arrival_date": flight["arrival_date"],
            "company": flight["company"],
            "duration": flight["duration"],
            "stops": flight["stops"],
            "emissions": flight["emissions"],
            "emission_comparison": flight["emission_comparison"],
            "price": flight["price"],
            "price_type": flight["price_type"],
            "departure_airport": flight["departure_airport"],
            "arrival_airport": flight["arrival_airport"],
        }
        flight_objects.append(flight_object)
    return flight_objects
