## Azure에 가입 및 컨테이너 생성
- 시크릿 모드로 http://portal.azure.com에 접속
- 로그인 후 홈에서 '리소스 만들기' --> '가상머신 만들기' --> Ubuntu Server 20.04 LTS x64 Gen2 선택하기

<img width='450' src='https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/e48cfdf7-1d59-4e80-9b10-eb9672279611'>
<img width='450' src='https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/43fb0907-e29f-46c1-b4bd-e8359027a6b7'>

- Inbound는 가상머신에 들어오는 것이고 Outbound가 나가는 것이다.
- 과금은 Outbound에 대해 물고 Inbound에 대해서는 물지 않아서 방산 업체가 CCTV 정보를 넣고 문제가 생긴 지점만 꺼내서 쓰기도 한다

<br>

<img width='450' src='https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/880376c3-e475-4c55-8904-577d387e27ba'>
<img width='450' src='https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/29d78fa5-eeef-4103-8d87-36cf54cad6d5'>

- 디스크부터 나머지 옵션들에 대해서는 기본으로 설정하고 그대로 넘어간다
- 가상 머신 만들기 --> 설치 --> 배포가 완료됨

<br><br>

## 가상 컴퓨터 Ubuntu 서버 구성

<img width="400" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/f6afbc96-0db8-43fb-a473-2549e3c1fcdd">
<img width="400" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/69b96413-d496-4320-af65-36e97a2d5c78">

- 만들어진 가상 머신(Ubuntu)에서 '연결'을 눌러 이동한다
- 생성된 가상머신(Ubuntu)의 연결에 원시 SSH를 선택하고 3번 'SSH 명령 복사 및 실행'에 있는 창을 선택한다
- 3번에서 SSH를 복사해서 terminal에서 실행시켜 공용 IP주소로 접속할 수 있다

<br>

<img width='750' src='https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/581f73af-e337-4d76-b6a4-3d44aa74e69e'>

- 접속 시에는 만들어 둔 비밀번호를 입력해야 접속이 허용된다

<br>

<img width='750' src='https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/12fbb452-8c8e-4c0d-83bb-05c9a5f8cff4'>

- Apt-get update는 업데이트를 하는 요청인데 처음에는 Block되는 것을 확인할 수 있다

<br>

<img width='750' src='https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/a74ece81-49a4-48ef-a1e5-9ef34b06c923'>

- sudo는 Super Do의 줄임말로 이를 앞에 붙여서 명령어를 관리자 권한으로 실행한다

<br><br>

## Docker

<img width='500' src='https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/4e1f64db-486f-4fcb-bd7e-68f7ef352699'>

- 서버 가상화 --> 운영 체제가 2개씩 쌓이는 것에도 overhead가 있네? --> 컨테이너 개념이 생겨남
- 내 자리에서 컨테이너를 만들고 컨테이너 환경에서 작업하고 환경 세팅하고 컨테이너 자체를 서버에 날리는 방식으로 해서 오류가 발생하지 않게 만들었다


```
sudo apt-get install ca-certificates curl gnupg
```
- certificates : 안전한 통신을 위해 필요한 인증서가 포함
- curl : 명령 줄에서 데이터를 전송하는 도구로, 주로 URL을 통해 데이터를 다운로드하거나 업로드하는 데 사용
- gnupg : 개인 정보 및 데이터의 암호화 및 디지털 서명에 사용되는 오픈 소스 암호화 소프트웨어, 안전한 통신 및 데이터 보호

- Ubuntu에 Docker 설치 관련 오피셜 Documents: https://docs.docker.com/engine/install/ubuntu/

### 1. Set up Docker's apt repository
```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```
```
# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

### 2. Install the Docker packages
```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### 3. Verify that the Docker Engine installation is successful
```
sudo docker run hello-world
```

<br><br>

## Docker Image 불러오기

<img width="750" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/ebee5075-068a-4641-81e4-84892de5bd30">

```
sudo docker pull ubuntu:18.04    # 18.04 버전의 ubuntu image를 로컬 시스템에 내려받음
sudo docker images               # 현재 시스템에 로컬로 저장된 Docker 이미지 목록을 표시
```

- docker pull : Docker 이미지를 Docker Hub 또는 다른 Docker 레지스트리로부터 로컬 시스템에 내려받습니다

<br><br>

## Docker Container 생성 및 Process 실행

```
docker run -it --name demo1 ubuntu:18.04 /bin/bash 
 
docker run -it -d --name demo2 ubuntu:18.04 

docker exec -it demo2 /bin/bash
 
docker run --name demo3 -d busybox sh -c "while true; do $(echo date); sleep 1; done" 
 
docker logs demo3

docker logs demo3 -f 
```

## Docker Container 관리

<img width="937" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/f82f9250-cf97-4d1a-93d3-34ccbbd637ca">

```
sudo docker ps               # Docker Container의 '현재 실행 중인' 목록을 출력, ps(processes)의 약어

sudo docker ps -a            # -a 옵션으로 중지되어 있는 목록까지도 출력 

sudo docker stop (name)      # 실행 중인 컨테이너의 프로세스를 중지하고 컨테이너의 상태를 'Exited'로 변경
                             # 나중에 다시 실행시킬 수 있음

sudo docker rm (name)        # 중지된 컨테이너를 삭제할 때 사용, stop을 먼저 하고 사용해야 함
```

<br>

## Docker Image 삭제

<img width="656" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/4d2f5c40-f53e-4d1f-9baa-96323f503f3c">

```
sudo docker images           # 현재 Docker에 

sudo docker rmi (image name) # 해당 이름의 image를 삭제
```

- 위의 명령어를 통해 image도 Docker에서 삭제할 수 있다
- 이 때 ubuntu와 같이 버젼이 있는 경우에는 버젼을 옆에 적어줘야 삭제가 제대로 진행된다

<br>

## Docker Image, Dockerfile

- Docker Image : 어떤 애플리케이션에 대해, 단순히 코드 뿐만 아니라 그 애플리케이션과 dependent한 모든 것을 함께 packaging한 데이터
- Docker File : 사용자가 Docker Image를 쉽게 만들 수 있도록 제공하는 템플릿

```
cd $HOME                # home directory로 이동
pwd                     # 현재 디렉토리 확인
mkdir docker-practice   # docker-practice라는 폴더 생성
cd docker-practice      # docker-practice 폴더로 이동
touch Dockerfile        # Dockerfile이라는 빈 파일을 생성
ls                      # 해당 디렉토리의 파일 목록을 출력
```

## Dockerfile 기본 명령어
#### 1. FROM
- Dockerfile이 Base Image로 어떠한 이미지를 사용할 것인지를 명시하는 명령어

```python
FROM <image>[:<tag>] [AS <name>]

# example
FROM ubuntu
FROM ubuntu:18.04
FROM nginx:latest AS ngx
```

#### 2. COPY
- <src>의 파일 혹은 디렉토리를 <dest> 경로에 복사하는 명령어

```python
COPY <src> ... <dest>

# example
COPY a.txt /some-directory/b.txt       # 파일 복사
COPY my-directory /some-directory-2    # 디렉토리 복사
```

#### 3. RUN
- 명시한 커맨드를 Docker Container에서 실행하는 것을 명시하는 명령어
- 환경을 설정하기 위해 실행할 때 한 번 시행되는 명령어

```python
RUN <command>
RUN ["executable-command", "parameter1", "parameter2"]

# example
RUN pip install torch
RUN pip install -r requirements.txt
```

#### 4. CMD
- 명시한 커맨드를 Docker Container가 시작될 때, 실행하는 것을 명시하는 명령어
- 하나의 Docker Image에서는 하나의 CMD만 실행할 수 있다는 점에서 RUN 명령어와 다르다

```python
CMD <command>
CMD ["executable-command", "parameter1", "parameter2"]

# example
CMD python main.py
```

#### 5. WORKDIR
- 이후 작성될 명령어를 Container 내의 어떤 디렉토리에서 수행할 것인지를 명시하는 명령어
- 해당 디렉토리가 없다면 생성한다

```python
WORKDIR /path/to/workdir

# example
WORKDIR /home/demo
```

#### 6. ENV
- Container 내부에서 지속적으로 사용될 Environment Variable(환경 변수)의 값을 설정하는 명령어

```python
ENV <key> <value>
ENV <key>=<value>

# example
RUN local-gen ko_KR.UTF-8
ENV LANG ko_KR.UTF-8
ENV LANGUAGE ko_KR.UTF-8
ENV LC_ALL ko_KR.UTF-8
```

#### 7. EXPOSE
- 컨테이너에서 뚫어줄 port/protocol을 지정할 수 있다
- protocol을 지정하지 않으면 TCP가 default로 설정된다

```python
EXPOSE <port>
EXPOSE <port>/<protocol>

# example
EXPOSE 8080
```
#### example

<img width="750" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/763a3fb7-0763-4a15-8914-18b6109bacfc">

<br><br>

## Build Docker Image from Dockerfile

<img width="850" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/5305db68-26e7-4260-b4dd-be7c9b4397c3">

```python
sudo docker build -t my-image:v1.0.0 . # 마지막 .은 경로를 말하는 것이므로 한 칸 뛰고 적어야 한다

ls -al                  # 디렉토리에 파일로 만들어진 것이 아니다
sudo docker images      # image로 만들어진 것이다
```

- Docker Image를 빌드하고 나면 디렉토리에 생성되는 것이 아니다(ls -al을 해도 나오는게 없다)
- sudo docker images를 하면 생성된 Docker Image가 목록에 있는 것을 발견할 수 있다

<img width="520" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/b9ed79d6-6fdd-42ae-a575-f8a9323832ff">

```python
sudo docker run my-image:v1.0.0    # 생성했던 image를 실행시킨다
```

- my-image의 실행 결과 CMD ["echo", "Hello World"]가 실행되어 출력되는 것을 확인할 수 있다
- 원래는 이런식으로 사용하지 않지만 build와 run이 제대로 작동하는지 확인하기 위한 용도의 example

<br><br>

## Docker Image Registry(저장소)

- Registry를 만들면 해당 저장소에 만든 이미지를 올릴 수 있다

<br>

<img width="750" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/d59b594c-6479-42c2-9aa1-99e4ac0f4c1a">

```python
docker run -d -p 5000:5000 --name registry registry
# 내부 5000, 외부 5000으로 port를 열어준다 
# registry를 registry라는 이름으로 가져오겠다
```

- Docker registry를 띄운다

<br>

## Docker Image Tag & Push

### 1. localhost에 tag & push
<img width="750" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/3a662d54-065c-49ff-8335-4e1631552350">
<img width="550" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/05661fa4-f624-4365-b19a-c76f2c7513e6">

```python
docker tag my-image:v1.0.0 localhost:5000/my-image:v1.0.0     # tag를 다는 코드

sudo docker images | grep my-image                            # 전체 images들 중 my-image를 포함한 부분을 추출
```
- 내 로컬 시스템에 있는 my-image를 방금 생성한 registry를 바라보도록 tag한다
- tag를 어디로 하고 push하는 지에 따라 만든 image를 어디에 연결할 것인지를 정할 수 있다
- docker images로 전체 이미지 목록을 보면 registry, my-image, localhost:5000/my-image가 있는 것을 볼 수 있다

<br>

<img width="685" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/608b1c2a-a736-44fe-a18b-3eb5cc3c2477">

```python
docker push localhost:5000/my-image:v1.0.0  
```
- 위의 명령어를 통해 push를 진행할 수 있다

### 2. Docker Hub에 tag & push

<img width="750" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/d1f7a0b8-6b24-4ffb-8d28-a03f43922148">

```python
docker login                                                # docker에 로그인을 시도
                                                            # email이 아니라 username과 접속에 필요한 password를 사용

sudo docker tag my-image:v1.0.0 kidong98/my-image:v1.0.0    # docker hub로 tag

sudo docker images                                          # images 목록에 kidong98/my-image:v1.0.0이 생긴 것을 볼 수 있다
```

<img width="750" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/9b28551e-ae82-4859-8649-9fe1bb359eeb">

```python
docker push kidong98/my-image:v1.0.0          # docker Hub에 tag되어 있는 것을 push해서 올린다

# sudo docker push kidong98/my-image:v1.0.0   # 이런 식으로 sudo가 앞에 붙으면 오류가 발생한다!
```

<img width="587" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/60687311-41c5-4f49-8bad-f51d60957923">

- Docker Hub에서 확인하면 image가 repository에 업로드된 것을 확인할 수 있다
