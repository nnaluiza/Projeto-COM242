import json
from database import MongoDBBase
from flask import Blueprint, jsonify, request
from helper import ObjectIdEncoder


class CarService(MongoDBBase):
    """Class for connecting to the 'cars' collection in MongoDB."""

    def __init__(self):
        super().__init__("car", "cars")

    def create_car_object(self, document):
        try:
            super().create(document)
        except Exception as e:
            raise e

    def get_all_cars(self, filter=None):
        cars = []
        for document in super().read(filter=filter):
            cars.append(document)
        return cars

    def get_cars(self, filter=None):
        return super().read(filter=filter)[0]

    def delete_cars(self, filter):
        try:
            super().delete(filter)
        except Exception as e:
            raise e


car_routes = Blueprint("cars", __name__)


@car_routes.route("/", methods=["GET"])
def get_all_cars():
    """Get all cars from the collection."""
    car_service = CarService()
    cars = car_service.get_all_cars()
    json_data = json.loads(json.dumps(cars, cls=ObjectIdEncoder))
    return json_data


@car_routes.route("/car", methods=["POST"])
def create_car():
    """Create a new car in the collection."""
    car_service = CarService()
    car_document = request.json
    car_service.create_car_object(car_document)
    return jsonify({"message": "Car created successfully."})


@car_routes.route("/getcars")
def get_cars():
    car_service = CarService()
    filter = request.get_json()["filter"]
    cars = car_service.get_all_cars(filter=filter)
    json_data = json.loads(json.dumps(cars, cls=ObjectIdEncoder))
    return json_data


@car_routes.route("/car/", methods=["DELETE"])
def delete_car():
    car_service = CarService()
    filter = request.get_json()["filter"]
    try:
        car_service.delete_cars(filter)
        return 1
    except Exception as e:
        raise e
