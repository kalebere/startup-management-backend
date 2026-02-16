from pymongo.mongo_client import MongoClient

client = MongoClient("mongodb+srv://sahilkalebere:sahilkalebere@cluster0.m1yz5js.mongodb.net/?appName=Cluster0")

startup = client["startup_db"]
auth_collection = startup["auth"]


__all__=[
    "auth_collection"
]