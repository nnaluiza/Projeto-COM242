import json
import os
import sys

import pymongo
from flight_crawl import run
from flight_helper import extract_flight_data, read_arguments_from_file
from playwright.sync_api import sync_playwright
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# # Create a MongoClient object with the MongoDB credentials.
# client = pymongo.MongoClient("localhost", 27017, username="root", password="password")

# Create a mongo client remotelly using mongo atlas
uri = "mongodb+srv://root:WGz8fNrUjAohWpre@cluster0.y0pssa2.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Get the database and collection.
db = client.flight
flights = db.flights

## Retrieve default flights args to ṕopulate the collection
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "flight_args/default_cities.txt")

arguments = read_arguments_from_file(filename)

# Create a list to store the flight objects.
flight_objects = []

for args in arguments:
    from_place = args[0]
    to_place = args[1]
    departure_date = args[2]
    return_date = args[3]

    with sync_playwright() as playwright:
        data = run(playwright, from_place, to_place, departure_date, return_date)
        list_of_flights = extract_flight_data(data)
        for obj in list_of_flights:
            obj["from_place"] = from_place
            obj["to_place"] = to_place
            db.flights.insert_one(obj)
