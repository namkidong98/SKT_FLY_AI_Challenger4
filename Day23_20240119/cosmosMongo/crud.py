import os, sys
from random import randint
import pymongo
from dotenv import load_dotenv

load_dotenv()
CONNECTION_STRING = os.environ.get("COSMOS_CONNECTION_STRING")
DB_NAME = "products"
COLLECTION_NAME = "books"

client = pymongo.MongoClient(CONNECTION_STRING)

db = client[DB_NAME]
if DB_NAME not in client.list_database_names():
    # DB 컬렉션에서 공유할 수 있는 400RU 처리량의 데이터베이스 생성
    db.command({"customAction" : "CreateDatabase", "offerThroughput" : 400})
    print("생성된 db : '{}'\n".format(DB_NAME))
else:
    print("db 사용 : '{}'\n".format(DB_NAME))

# Collection
collection = db[COLLECTION_NAME]
if COLLECTION_NAME not in db.list_collection_names():
    #creates a unsharded collection that uses the DBs shared throughput 
    db.command(
        {"customAction" : "CreateCollection", "collection" : COLLECTION_NAME}
    )
    print("생성된 컬렉션(collection) : '{}'\n".format(COLLECTION_NAME))
else:
    print("컬렉션(collection) 사용 : '{}'\n".format(COLLECTION_NAME))