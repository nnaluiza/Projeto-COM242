import json
import os
import sys

import pymongo
from playwright.sync_api import sync_playwright
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from flight_crawl import run
from flight_helper import extract_flight_data

uri = "mongodb+srv://root:WGz8fNrUjAohWpre@cluster0.y0pssa2.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi("1"))

# Get the database and collection.
db = client.flight
flights = db.flights


def get_unfound_flight(from_place, to_place, departure_date, return_date):
    with sync_playwright() as playwright:
        data = run(playwright, from_place, to_place, departure_date, return_date)
        list_of_flights = extract_flight_data(data)
        for obj in list_of_flights:
            obj["from_place"] = from_place
            obj["to_place"] = to_place
            db.flights.insert_one(obj)
        return list_of_flights
