from azure.cosmos import CosmosClient, exceptions, PartitionKey
import os, json
from dotenv import load_dotenv

load_dotenv() # .env에 저장된 값들 로딩

URL = os.environ.get("ACCOUNT_URI")
KEY = os.environ.get("ACCOUNT_KEY")
client = CosmosClient(URL, credential=KEY)
DATABASE_NAME = 'customerList'

try:
    database = client.get_database_client(DATABASE_NAME)
except exceptions.CosmosResourceExistsError:
    database = client.get_database_client(DATABASE_NAME)

CONTAINER_NAME = 'products'
container = database.get_container_client(CONTAINER_NAME)

for item in container.query_items(
        query='SELECT * FROM mycontainer r Where r.id="item3"',
        enable_cross_partition_query=True):
    print(json.dumps(item, indent=True))