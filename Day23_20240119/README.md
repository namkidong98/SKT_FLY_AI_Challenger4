<img width="466" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/694ea02c-6e3d-468e-be71-6f57e19092d2"># Azure Cosmos DB

## Azure에서 사전 설정

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

## VSCode 사전 설정 

```
# 1. 가상 환경
python -m venv venv       # 가상환경 만들기
.\venv\Scripts\activate   # 가상 환경 접속

# 2. 라이브러리 설치
pip install pymongo python-dotenv

# 3. .env 파일 생성 & 연결 문자열 넣어주기
```

<br>

## CRUD Operation

```
# 1. crud.py 파일 생성
python crud.py            # 파일 실행

# 2. insert-document 파일 생성
python insert-document.py # 파일 실행

# 3. insert-document 파일 생성
python insert-document.py # 파일 실행

# 4. insert-multidocument 파일 생성
python insert-document.py # 파일 실행

# 5. select-document 파일 생성
python select-document.py # 파일 실행

# 6. update-document 파일 생성
python update-document.py # 파일 실행

# 7. delete-document 파일 생성
python delete-document.py # 파일 실행행
```

<br>

<img width="600" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/232efb9e-9663-4f63-a71e-115954289e21">

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

<br>

<img width="600" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/4f21f7c0-eea6-42dd-a30b-573acace2bdc">

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

<img width="600" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/7e8041cf-f0fc-4c8b-b731-3eff35c9e5d4">

```python
# insert-multidocument.py
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
books = [
    {
        "_id" : 1,
        "category" : "Marketing, Sales",
        "name" : "마케팅 불변의 법칙",
        "author" : "알 리스, 잭 트라우트",
        "publisher" : "비즈니스"
    },
    {
        "_id" : 2,
        "category" : "Marketing, Sales",
        "name" : "정상에서 만납시다",
        "author" : "지그지글러",
        "quantity" : 1,
    }
]
result = collection.insert_many(books)
print("추가된 문서 _id : {}\n".format(result.inserted_ids[0]))

```

<br>

<img width="600" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/c2775c82-2f21-4a91-b455-df6e11f695c9">
<img width="635" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/9512775c-2080-4dbe-9dbe-0520a11e1c79">

```python
# select-document.py
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
```

<br>

<img width="575" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/4c01ef9b-321f-4533-ab3c-d8747598f8ac">

```python
# update-document.py
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

collection.update_one(findValue, newValue) # 찾은 데이터 하나만 바꿔줌
# collection.update_many(findValue, newValue) # 여러 개를 바꿔주려는 경우 
```

<br>

<img width="650" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/7b32dd5f-9853-4dc0-bccf-98af344d19d9">

```python
# delete-document.py
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
```

<br>

# Azure DB for MySQL

<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/e0d11d47-090f-4233-bdc0-6aebe4f3165f">
<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/4b8ab2fd-e87a-4516-8f51-30c2c9cfef12">
<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/a547f2ed-05f0-47f5-8824-1c639317e6f8">
<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/0e61b5a9-4c24-4223-b452-192d40ae3c5d">
<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/ec4949a5-fdab-46e3-8d79-244bace7e374">

<br>

## MySQL WorkBench

<img width="572" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/60255055-5888-4a0f-be5b-83b6f7d988d1">

## 
