from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from cars_crawl import crawler_carros

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
db = client.car
cars = db.cars


# TODO Put the args that the crawler must receive as function args
def get_unfound_cars():
    ## TODO replace with the right function name
    new_cars = crawler_carros()
    for obj in new_cars:
        db.cars.insert_one(obj)
    return new_cars
