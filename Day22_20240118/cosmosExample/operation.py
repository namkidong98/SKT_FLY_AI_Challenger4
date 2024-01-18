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
try:
    container = database.create_container(
        id = CONTAINER_NAME,
        partition_key=PartitionKey(path="/productName")
    )
except exceptions.CosmosResourceExistsError:
    container = database.get_container_client(CONTAINER_NAME)
except exceptions.CosmosHttpResponseError:
    raise

for i in range(1, 10):
    container.upsert_item( # 있는 거는 업데이트, 없으면 생성
        {
            'id' : 'item{0}'.format(i),
            'productName' : 'Laptop',
            'productModel' : 'Model {0}'.format(i)
        }
    )