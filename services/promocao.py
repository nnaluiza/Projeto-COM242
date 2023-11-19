from hotel import HotelService
from flight import FlightService
from cars import CarService


class PackageService:
    def create_package(self, city):
        hotels = HotelService.get_all_hotels(filter={"city": city}).sort(
            key=lambda hotel: hotel.price
        )[:3]
        flights = FlightService.get_all_flights(filter={"city": city}).sort(
            key=lambda flight: flight.price
        )[:3]
        cars = CarService.get_all_cars(filter={"city": city}).sort(
            key=lambda car: car.price
        )[:3]
        return {"hotels": hotels, "flights": flights, "cars": cars}
