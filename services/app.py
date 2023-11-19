from flask import Flask, request, jsonify

# from flight_service import FlightService
# from user_service import UserService

from flight import flight_routes
from hotel import hotel_routes
from cars import car_routes

app = Flask(__name__)

# Register the flight service endpoints
app.register_blueprint(flight_routes, url_prefix="/flights")

# Register the hotel service endpoints
app.register_blueprint(hotel_routes, url_prefix="/hotels")

# Register the car service endpoints
app.register_blueprint(car_routes, url_prefix="/cars")

# # Register the user service endpoints
# app.register_blueprint(UserService.blueprint)

if __name__ == "__main__":
    app.run(debug=True, port=8000, use_reloader=False)
