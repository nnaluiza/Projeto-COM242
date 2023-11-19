import os

from car_helper import read_arguments_from_file
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
db = client.car
cars = db.cars

## Retrieve default cars args to ṕopulate the collection
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "car_args/default_cities.txt")

arguments = read_arguments_from_file(filename)


# Create a list to store the car objects.
car_objects = []
for args in arguments:
    # TODO check the arguments that will be passed to the crawler
    # and build it from the args file

    ## TODO replace with the right function call
    car_objects = crawler_carros()
    for obj in object:
        db.cars.insert_one(obj)
