import time
import subprocess

while True:
    # Run fetch_and_save_cars_to_mongo
    subprocess.run(["python3", "./carros/fetch_and_save_cars_to_mongo.py"])

    # Wait for 3 hours
    time.sleep(10800)  # 3 hours in seconds

    # Run fetch_and_save_flights_to_mongo
    subprocess.run(["python3", "./flights/fetch_and_save_flights_to_mongo.py"])
    subprocess.run(["python3", "./flights/clear_database.py"])

    # Wait for 3 hours
    time.sleep(10800)  # 3 hours in seconds

    # Run fetch_and_save_hotels_to_mongo
    subprocess.run(["python3", "./hoteis/fetch_and_save_hotels_to_mongo.py"])

    # Wait for 3 hours
    time.sleep(10800)  # 3 hours in seconds
