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

collection.delete_one(findValue) # 찾은 데이터 하나만 삭제
# collection.delete_many(findValue) # 찾은 데이터 모두 삭제