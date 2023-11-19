import json
import os
import sys

import pymongo
from hotel_crawl import crawler_hoteis
from hotel_helper import read_arguments_from_file
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Create a mongo client locally (usefull to test)
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

# Get the database and collection
db = client.hotel
hotels = db.hotels

## Retrieve default hotel args to populate the collection
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "hotel_args/default_cities.txt")

arguments = read_arguments_from_file(filename)
print(arguments)
hotels = []

for args in arguments:
    city = args[0]
    people = args[1]
    nights = args[2]
    hotels = crawler_hoteis(city, people, nights)
    try:
        for obj in hotels:
            obj["cidade"] = city
            obj["people"] = people
            obj["nights"] = nights
            db.hotels.insert_one(obj)
        print("Hoteis salvos no banco")
    except Exception as e:
        raise e
