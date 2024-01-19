## Azure Cosmos DB
<img width="700" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/6921f30f-ff93-47e6-b9d7-611906509a63">
<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/a5715c9d-7c9a-4513-ac5f-f7baa574ac43">

```
# 1. 리소스 그룹 만들기, Azure Cosmos DB 계정 만들기
resourceGrp="mycosmosdbmongo-rg"
location="eastus"
cosmosdbAccount="mycmdbkd"
az group create --name $resourceGrp --location $location

# 2. MongoDB 형태의 Cosmos DB 생성
az cosmosdb create --name $cosmosdbAccount --resource-group $resourceGrp --locations regionName=$location --kind MongoDB

# 3. Azure Cosmos DB 리소스에서 연결 문자열(connection strings) 유형의 키를 나열
az cosmosdb keys list --type connection-strings --resource-group $resourceGrp --name $cosmosdbAccount
```

```python
# 1. 가상 환경
python -m venv venv       # 가상환경 만들기
.\venv\Scripts\activate   # 가상 환경 접속

# 2. 라이브러리 설치
pip install pymongo python-dotenv

# 3. .env 파일 생성 & 연결 문자열 넣어주기

# 4. crud.py 파일 생성
python crud.py            # 파일 실행

# 5. insert-document 파일 생성
python insert-document.py # 파일 실행
```

```python
# crud.py
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
```

```python
# insert-document.py
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
```
<br>

<img width="600" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/232efb9e-9663-4f63-a71e-115954289e21">
<img width="600" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/4f21f7c0-eea6-42dd-a30b-573acace2bdc">

## 
