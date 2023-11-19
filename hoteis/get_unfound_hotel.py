import json
import os
import sys

import pymongo
from hotel_crawl import crawler_hoteis
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://root:WGz8fNrUjAohWpre@cluster0.y0pssa2.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi("1"))
# Get the database and collection.
db = client.hotel
hotels = db.hotels


def get_unfound_hotel(city, people, nights):
    hotels = []
    # TODO replace with the right function
    hotels = crawler_hoteis(city, people, nights)
    return hotels
