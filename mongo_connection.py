from pymongo import MongoClient


def connect():
    global db
    mongodb_port = 27017
    client = MongoClient('localhost',mongodb_port)
    db = client.big_data


def get_events_collection():
    return db.events


connect()