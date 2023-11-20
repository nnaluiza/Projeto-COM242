import json
from database import MongoDBBase
from flask import Blueprint, jsonify, request
from helper import ObjectIdEncoder

# from hoteis.get_unfound_hotel import get_unfound_hotel


class HotelService(MongoDBBase):
    """Class for connecting to the 'hotels' collection in MongoDB."""

    def __init__(self):
        super().__init__("hotel", "hotels")

    def create_hotel(self, document):
        try:
            super().create(document)
        except Exception as e:
            raise e

    def get_all_hotels(self, filter=None):
        hotels = []
        for document in super().read(filter=filter):
            hotels.append(document)
        return hotels

    def get_hotel(self, filter=None):
        return super().read(filter=filter)[0]

    def delete_hotels(self, filter):
        try:
            super().delete(filter)
        except Exception as e:
            raise e


hotel_routes = Blueprint("hotels", __name__)


@hotel_routes.route("/", methods=["GET"])
def get_all_hotels():
    hotel_service = HotelService()
    hotels = hotel_service.get_all_hotels()
    json_data = json.loads(json.dumps(hotels, cls=ObjectIdEncoder))
    return json_data


@hotel_routes.route("/hotel", methods=["POST"])
def create_hotel_routes():
    """Create a new flight in the collection."""
    hotel_service = HotelService()
    hotel = request.json
    hotel_service.create_flight_object(hotel)
    return jsonify({"message": "Hotel created successfully."})


@hotel_routes.route("/gethotels")
def get_hotels():
    filter = request.get_json()["filter"]
    hotel_service = HotelService()
    hotels = hotel_service.get_all_hotels(filter=filter)
    json_data = json.loads(json.dumps(hotels, cls=ObjectIdEncoder))
    return json_data


@hotel_routes.route("/hotel/", methods=["DELETE"])
def delete_hotel():
    hotel_service = HotelService()
    filter = request.get_json()["filter"]
    try:
        hotel_service.delete_hotels(filter)
        return "Hotels deleted!"
    except Exception as e:
        raise e


# @hotel_routes.route("/crawler", methods=["GET"])
# def call_crawler():
#     filter = request.get_json()["filter"]
#     try:
#         city = filter["city"]
#         people = filter["people"]
#         nights = filter["nights"]
#         new_hotels = get_unfound_hotel(city, people, nights)
#         json_data = json.loads(json.dumps(new_hotels, cls=ObjectIdEncoder))
#         return json_data
#     except Exception as e:
#         raise e
