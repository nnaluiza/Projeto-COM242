import json
from database import MongoDBBase
from flask import Blueprint, jsonify, request
from helper import ObjectIdEncoder


class FlightService(MongoDBBase):
    """Class for connecting to the 'flights' collection in MongoDB."""

    def __init__(self):
        super().__init__("flight", "flights")

    def create_flight_object(self, document):
        try:
            super().create(document)
        except Exception as e:
            raise e

    def get_all_flights(self, filter=None):
        flights = []
        for document in super().read(filter=filter):
            flights.append(document)
        return flights

    def get_flight(self, filter=None):
        return super().read(filter=filter)[0]

    def delete_flights(self, filter):
        try:
            super().delete(filter)
        except Exception as e:
            raise e


flight_routes = Blueprint("flights", __name__)


@flight_routes.route("/", methods=["GET"])
def get_all_flights():
    """Get all flights from the collection."""
    flight_service = FlightService()
    flights = flight_service.get_all_flights()
    json_data = json.loads(json.dumps(flights, cls=ObjectIdEncoder))
    return json_data


@flight_routes.route("/flight", methods=["POST"])
def create_flight():
    """Create a new flight in the collection."""
    flight_service = FlightService()
    flight_document = request.json
    flight_service.create_flight_object(flight_document)
    return jsonify({"message": "Flight created successfully."})


@flight_routes.route("/getflights")
def get_flights():
    flight_service = FlightService()
    filter = request.get_json()["filter"]
    flights = flight_service.get_all_flights(filter=filter)
    json_data = json.loads(json.dumps(flights, cls=ObjectIdEncoder))
    return json_data


@flight_routes.route("/flight/", methods=["DELETE"])
def delete_flight():
    flight_service = FlightService()
    filter = request.get_json()["filter"]
    try:
        flight_service.delete_flights(filter)
        return 1
    except Exception as e:
        raise e
