# 배포 슬롯(Deployment Slots)
- 배포 슬롯은 자체 호스트 이름을 가진 라이브 앱
- 웹앱이 표준, 프리미엄 또는 격리 서비스 계층의 App Service 계획을 사용하는 경우에만 배포 슬롯 제공
- 앱 컨텐츠 및 구성은 프로덕션 슬롯과 다른 슬롯 간에 교환 가능
- 새로운 기능을 Production slot이 아닌 다른 slot에서 배포할 경우, 애플리케이션의 변경 사항에 대한 유효성 검사 가능

<br>

## 실습 - 배포 슬롯
1. 웹 앱 만들기
2. 로컬 Git 리포지토리를 이용한 Git 배포 구성
3. Git 클라이언트 구성 및 웹 앱 소스 코드 복제
4. Production 슬롯에 앱을 배포하도록 git remote 구성
5. 새 Staging 슬롯 만들기
6. 새 Staging 슬롯에 Git 배포 구성
7. Staging 슬롯에 앱을 배포하도록 git remote 구성
8. 앱 소스 코드 수정 및 Staging 슬롯에 배포
9. 슬롯 설정 구성 및 교환

<br>

# Azure Container Instance(ACI)

<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/03fd8436-f0bb-4971-b4e2-b1e40bf5dd52">
<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/ddee79a2-126b-42da-8ecd-752579245792">
<img width="900" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/28f68a40-b209-4fb1-8c68-b5422ec837ab">

<br><br>

# Docker, Docker Hub

## 1. Ubuntu 가상 머신 설치 및 Docker 설치
<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/dffbcf46-7357-414d-8690-986a35602deb">
<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/fc6783cf-b6ca-40a8-b98a-79dec563095c">

- 가상 머신을 Azure에서 만든다

<br>

<img width="900" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/6c6ab848-5656-4a98-b9b4-d001e7ba0fdf">

```
경로\.ssh> ssh -i (가상머신 이름_key.pem) (사용자 이름)@(공용 IP주소)

# example
PS C:\Users\2023-PC(T)-10\.ssh> ssh -i dockerubuntu20_key.pem kidong@20.42.40.226
```

- C드라이브 - User - .ssh 폴더에 key.pem 파일을 넣어주고 Powershell에서 위의 명령어를 실행하면 가상 머신에 접속이 가능해진다

<br>

```
# 도커 설치 관련 링크 : https://docs.docker.com/engine/install/ubuntu/ 
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin



# 잘 설치되었는지 아래의 명령어들로 확인해볼 수 있다
sudo systemctl status docker
apt-cache policy docker-ce
sudo docker run hello-world
```

<img width="600" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/3a046aec-6424-463e-ae49-9cf2814e779e">
<img width="600" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/ed0cb56c-69b9-42c4-b93d-24f70c4ca9c7">
<img width="600" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/2cecb49e-6442-4676-acc8-491e680a17e3">

<br>

### node:20-alpine 예제
<img width="750" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/743c4456-ce5f-4e25-898f-324c13e61294">
<img width="750" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/1fc2b8e8-bfc4-4719-99f3-c14cd949fcc8">

```
docker pull node:20-alpine        # permission denied 오류 발생
sudo docker pull node:20-alpine   # sudo를 추가해줘야 제대로 작동됨
sudo docker images
sudo docker run -it -d -p 8080:8080 --name=nodejs_app node:20-alpine  # 컨테이너 실행
```

## 2. Nginx 웹서버 만들기
<img width="600" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/e7be3b0c-b4ee-4444-a4aa-463ce1c0e492">
<img width="600" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/6fca3c5f-a1a7-4e49-9268-ea32d02d74b1">
<img width="600" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/1c376643-9ed5-4098-8b10-f5a32d5ba508">

```
# 링크 : https://hub.docker.com/_/nginx
sudo docker pull nginx:1.25.3-alpine
sudo docker images
sudo docker run --name nginx-srv -p 80:80 -d nginx:1.25.3-alpine

# net 상태를 표시
sudo apt install net-tools
netstat -tnlp
```

<br>

<img width="600" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/5f335551-9582-4448-a78d-f6f62dee7c50">
<img width="900" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/38477654-4b18-4821-be76-2549d5139b20">

- 기존에 가상 머신을 만들 때, ssh만 열었기 때문에 공용 IP로는 접속이 되지 않는다

<br>

<img width="900" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/5eefcfa5-5e12-4d5f-8a90-3d93176c3327">
<img width="600"  src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/742aee8c-ae04-40d2-88ab-f3f622112894">

- 인바운드 규칙에서 80 port(HTTP)를 열어줘야 web browser에서도 접속이 된

## 3. Dockerfile
- Dockerfile : 필요한 Docker image를 생성하기 위한 일련의 명령 또는 지침이 포함된 텍스트 파일
- 명령은 쓰여진 순서대로 실행되며(docker build) Docker image를 생성, 명령으로는 FROM, COPY, RUN, CMD 등이 있다

## 4. Apache 웹 서버 만들기

<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/a6455ceb-b312-4550-ba67-8656a869cff4">

```
vi Dockerfile                       # Dockerfile 작성
cat Dockerfile                      # Dockerfile 확인
sudo docker build -t apache2:1.0 .  # Dockerfile로 image 생성
sudo docker run 
```

```
FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update
RUN apt install -y apache2
RUN apt install -y apache2-utils
RUN apt clean

EXPOSE 80

CMD /usr/sbin/apache2ctl -D FOREGROUND
```

- Dockerfile을 작성하고 생성한 Dockerfile로 image 만들기

<img width="900" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/06ed85f7-9cc9-4c73-9813-5cee7fdcc911">
<img width="900" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/b2e74fce-4d26-4d71-8e53-f0b093bf6c0f">

- 기존에 돌고 있는 alpane을 멈추고 docker run을 해준다

<br>

<img width="900" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/1b09d5e0-81ee-4c7f-a882-0d2311cd03a2">
<img width="300" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/6bbaba6e-1b56-41b3-96e5-14f069b3a31b">

```
vim index.html
cat index.html
sudo docker ps -a  # 현재 실행중인 컨테이너 ID 확인
sudo docker stop (현재 실행중인 컨테이너 ID)
sudo docker run --name apache-srv -p 80:80 -d -v /home/kidong/apache_docker/html:/var/www/html apache2:1.0
```

```
<html lang="ko">
<head>
        <meta charset='utf-8'>
        <title>Apache 웹사이트 수정</title>
</head>
<body>
        <h3>Dockerfile을 이용한 Apache 웹사이트</h3>
</body>
</html>
```

- 위의 index.html이 있는 위치로 apache-srv라는 이름으로 docker 컨테이너를 실행시키면 위와 같이 나온다

<br>

# Azure Container Registry(ACR)

<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/6ae9bab1-1320-43fa-995a-d8a2b1fb89d4">
<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/e34c82a0-4a43-44ff-8e31-13623cdb3790">
<img width="714" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/45a14887-79ee-4da6-bcc7-5c109418ff3f">
<img width="626" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/5901a742-a0b5-4f00-adea-bb3c79cdc6dc">

```
az acr create --name mykdregistry --resource-group Legend-DuckEgg --sku standard --admin-enabled true
# Azure CLI에서 시작할 때는 az
# acr create                       : ACR을 만들겠다
# --name mykdregistry              : 다음으로 이름을 지정하겠다
# --resource-group Legend-DuckEgg  : 다음으로 리소스 그룹을 지정하겠다
# --sku standard                   : standard 계층을 사용하겠다
# --admin-enabled true             : root 권한을 활성하시키겠다

git clone https://github.com/MicrosoftDocs/mslearn-deploy-run-container-app-service
cd mslearn-deploy-run-container-app-service/node
cat Dockerfile 
az acr build --registry mykdregistry --image webimage .

# 내 레지스트리의 상태 확인
az acr show -n mykdregistry --resource-group Legend-DuckEgg
az acr check-health -n mykdregistry -y
```

<img width="1001" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/db2f3747-1ffd-4fa9-bd10-2a2fc8e43be9">
<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/18a602d4-a0eb-436e-9404-3a757b1731b5">
<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/69472e1e-ef2e-4016-b52d-f2653d820a35">


## Dockerfile, ACR을 이용한 ACI(Azure Container Instance) 구현
1. Azure CLI 실행
2. ACR(Azure Container Registry) 생성
3. Dockerfile을 이용하여 ACR에 이미지 업로드
4. ACI(Azure Container Instance) 생성

<br>

<img width="700" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/efc9ecf1-3e22-4ac6-b63d-d958dd1b184c">
<img width="700" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/f75e8f9f-4da8-42f0-899d-09a5c6c54540">

```
git clone https://github.com/Azure-Samples/aci-helloworld

cd aci-helloworld/app
vi index.html   # header 수정하기
cat index.html  # 수정된 것인지 확인

az group create --name rg-acr1 --location eastus
az acr create --resource-group rg-acr1 --name helloregistry01kd --sku Standard
az acr build --registry helloregistry01kd --image helloacr:v1 . # Dockerfile이 있는 곳에서
```

<img width="700" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/084d7d44-bf12-4b39-9387-2b21dc9ffb18">
<img width="700" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/e221392b-1ab6-49a0-878b-019ebf979229">
<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/d6e6cf29-eaca-42f0-87db-26a0db42c253">
<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/1ea64ea9-27a2-4571-b5a7-fe9615d213e2">
<img width="700" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/e7698906-29e9-45cb-83ed-5418ef16b443">

<br><br>

# Azure Cosmos DB SQL API 구성 요소
- 데이터 베이스 : Azure Cosmos DB SQL API에서 컨테이너 관리를 위한 논리적 단위
- 컨테이너 : 기본적인 스케일링 단위, Azure Cosmos DB SQL API는 자동으로 컨테이너의 데이터를 분할
- JSON 형식으로 컨테이너 안에 개별 문서가 저장된다
- 분할을 사용하기 위해서는 경로로 구성된 파티션 키(ex /firstname)가 사용된다

<br>

<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/aadc9db4-66aa-4508-803f-202f3d67633a">
<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/5f20746a-c0e1-4d71-87aa-1e1590c81987">
<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/b2891c8f-be8b-4c88-a10c-7751a3e16f62">

<br><br>

## CRUD Operation

<img width="900" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/444e2303-d566-46ac-b480-10de88072cfd">
<img width="900" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/fbeffc6e-0b37-47a4-b1ae-bd8b6d41c849">

<br><br>

## Python으로 컨테이너

```
# command prompt로 terminal을 하나 만들고
python -m venv venv      # 가상 환경 생성
.\venv\Scripts\activate  # 가상 환경 활성화
pip install azure-cosmos python-dotenv
pip install azure-identity

# .env 파일 생성
# operation.py 파일 생성
python operation.py
```

<img width="419" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/8972f40e-da72-4f71-94f3-2058b4e09dcb">
<img width="529" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/002d250e-e225-40ed-9f23-b0437cbc3374">

- 만든 cosmos DB API에서 Key를 복사해서 .env 파일의 ACCOUNT_URI에 넣는다
- Primary Key를 .env 파일의 ACCOUNT_KEY에 넣는다

```python
# operation.py 파일 생성
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
```

<br>

<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/a5b42403-9de5-4267-bc65-c2bf87099329">
<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/e6af45d3-1ae0-4e08-8ef6-af04d5e14ee7">
<img width="900" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/75e397c8-ffa7-47f2-83e5-34727468bee1">

- venv에 들어가서 .env 파일을 만들고 azure DB API에서 URI와 KEY를 가져와서 입력한다
- opeartion.py 파일을 만들고 모든 파일을 저장하고 python operation.py를 실행하면 Azure DB에 products가 생성된 것을 확인할 수 있다
- for문으로 9개의 product item이 추가되는 것도 확인할 수 있다

<br>

<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/4e1eb626-09f5-457b-ad7c-c40ca4faad46">
<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/057f994c-8c90-479a-b7d9-c6e6546be875">

```python
##-----operation-select.py------##
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
```

```python
##-----operation-select2.py------##
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

discontinued_items = container.query_items(
    query='SELECT * FROM products p WHERE p.productModel = @model',
    parameters= [
        dict(name='@model', value='Model 7')
    ],
    enable_cross_partition_query=True
)
for item in discontinued_items:
    print(json.dumps(item, indent=True))
```

- operation-select.py를 추가해서 query를 실행하면 해당하는 데이터가 출력되는 것을 확인할 수 있다
- operation-select2.py를 추가해서 query를 실행해도 해당하는 데이터가 출력되는 것을 확인할 수 있다
