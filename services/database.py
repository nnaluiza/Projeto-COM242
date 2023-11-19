import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class MongoDBBase:
    """Base class for connecting to MongoDB and performing CRUD operations."""

    def __init__(self, database_name, collection_name):
        self.client = MongoClient(
            "mongodb+srv://root:WGz8fNrUjAohWpre@cluster0.y0pssa2.mongodb.net/?retryWrites=true&w=majority",
            server_api=ServerApi("1"),
        )
        self.database = self.client[database_name]
        self.collection = self.database[collection_name]

    def create(self, document):
        """Insert a new document into the collection."""
        self.collection.insert_one(document)

    def read(self, filter=None):
        """Read documents from the collection."""
        if filter is None:
            return self.collection.find()
        else:
            return self.collection.find(filter)

    def update(self, filter, update):
        """Update documents in the collection."""
        self.collection.update_one(filter, update)

    def delete(self, filter):
        """Delete documents from the collection."""
        self.collection.delete_many(filter)

    def close(self):
        """Close the connection to MongoDB."""
        self.client.close()
