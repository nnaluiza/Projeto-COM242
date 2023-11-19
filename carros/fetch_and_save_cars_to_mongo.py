import os

from car_helper import read_arguments_from_file
from cars_crawl import crawler_carros
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
filename = os.path.join(dirname, "./carros_args/default_cities.txt")

arguments = read_arguments_from_file(filename)
print(arguments)

# Create a list to store the car objects.
car_objects = []

for args in arguments:
    # TODO check the arguments that will be passed to the crawler
    city = args[0]
    year_arrive = (args[1],)
    month_arrive = (args[2],)
    day_arrive = (args[3],)
    year_departure = (args[4],)
    month_departure = (args[5],)
    day_departure = args[6]

    car_objects = crawler_carros(
        city,
        year_arrive,
        month_arrive,
        day_arrive,
        year_departure,
        month_departure,
        day_departure,
    )

    try:
        for obj in object:
            db.cars.insert_one(obj)
    except Exception as e:
        raise e
