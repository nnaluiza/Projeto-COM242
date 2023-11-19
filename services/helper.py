import json
from bson.objectid import ObjectId


class ObjectIdEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)
