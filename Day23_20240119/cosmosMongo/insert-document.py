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
book = {
    "category" : "Computers, Technology",
    "name" : "MongoDB The Definitive Guide",
    "quantity" : 2,
    "sale" : False
},
result = collection.insert_many(book)
print("추가된 문서 _id : {}\n".format(result.inserted_ids[0]))