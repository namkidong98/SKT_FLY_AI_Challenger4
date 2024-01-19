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

# find_doc = collection.find_one({"category" : "Marketing, Sales"}) # 하나만 찾는 경우
# print(find_doc)

find_docs = collection.find({"category" : "Marketing, Sales"}) # 여러 개 찾는 경우
for doc in find_docs:
    print(doc)