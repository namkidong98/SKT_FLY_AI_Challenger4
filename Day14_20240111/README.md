## Azure에 가입 및 컨테이너 생성
- 시크릿 모드로 http://portal.azure.com에 접속
- 가상머신 만들기 (Ubuntu Server 20.04 LTS x64 Gen2)

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

<img width="400" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/69b96413-d496-4320-af65-36e97a2d5c78">

- Azure에서 생성된 가상머신(Ubuntu)의 연결에 들어가서 원시 SSH 창에 있는 공용 IP주소로 접속할 수 있다

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

#### abc
<img width="750" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/ebee5075-068a-4641-81e4-84892de5bd30">


Ubuntu 
```
sudo docker run -it --name demo1 ubuntu:18.04 /bin/bash
```


```
sudo docker run -it -d --name demo2 ubuntu:18.04
```
- -it : iteractive 옵션
- -d : demon 옵션
- 
