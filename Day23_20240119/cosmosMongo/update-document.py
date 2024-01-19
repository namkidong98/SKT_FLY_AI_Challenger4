import os, sys
from random import randint
import pymongo
from dotenv import load_dotenv

load_dotenv()
CONNECTION_STRING = os.environ.get("COSMOS_CONNECTION_STRING")
DB_NAME = "products"
COLLECTION_NAME = "books"

client = pymongo.MongoClient(CONNECTION_STRING)
db = client[DB_NAME] # 데이터 베이스
collection = db[COLLECTION_NAME] # Collection

findValue = {"category" : "Marketing, Sales"}
newValue = {"$set" : {"category" : "Business, Money"}}

collection.update_one(findValue, newValue)