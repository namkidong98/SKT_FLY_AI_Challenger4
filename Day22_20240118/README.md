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
