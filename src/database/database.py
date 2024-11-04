from pymongo import MongoClient
from decouple import config

client = MongoClient(config("MONGODB_URL"))

db = client[config("DB_NAME")]