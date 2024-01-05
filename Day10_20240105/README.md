## Ubuntu 설치
1. Hyper-V에서 빨리 만들기를 선택, 다운로드 받은 ubuntu iso 파일을 로드하고 "이 가상 컴퓨터에서 Windows 실행" 옵션 해제

<img width="877" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/f531e27f-3724-4999-8a6e-b658f88935c7">

<br> 

2. RAM은 4096B(4GB) 그대로, 하드 메모리 크기는 60GB로 설정

<br> 

3. 생성된 가상 컴퓨터를 실행하고 시스템 설정에서 username, password를 지정하고 '자동 로그인' 옵션은 해제(나중에 문제 발생할 수 있음)   
   cf) username과 password는 지속적으로 쓸 수 있으므로 꼭 외워둬야 한다
<img width="600" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/083f95c0-f20c-421b-beaa-889c2b5b449a">

<br> 

4. terminal에서 다음 명령어들을 실행하여 업데이트를 진행
```
# Apt-get update의 서버 변경
1. sudo vi /etc/apt/sources.list 로 파일 열고,
2. :%s/kr.archive.ubuntu.com/ftp.daumkakao.com
3. :wq
```
```
sudo apt-get update
sudo apt-get install vim
sudo apt-get upgrade
sudo apt-get install gparted
```
```
# Git 관련 다운로드 및 버젼 업데이트
sudo apt install git
sudo add-apt-repository ppa:git-core/ppa -y
git --version       # (2.28 이상이어야함 --> main으로 기본 default가 됨)

sudo add-apt-repository ppa:git-core/ppa -y
sudo apt-get install git -y
sudo apt-get update
```

<br> 

5. 고급세션 모드 사용할 수 있게 설정하기 (복사 붙여 넣기, 해상도 설정 등을 위한 작업)   
https://lucidmaj7.tistory.com/343

<br> 

## Git
이전 자료 링크: https://github.com/namkidong98/SKT_FLY_AI_Challenger4/tree/main/Day09_20240104   

#### 4) Github 가입하고 token 만들기
- Sign Up으로 가입 후 로그인
- Github 프로필을 누르고 들아가서 좌측 맨 아래에 Developer Settings를 선택
- Personal access tokens --> Tokens(classic) --> Generate new token(classic)

<img width="830" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/e95af1d7-9eb5-4c28-b23a-9f77dc4e0e0f">

<br> 

- 원하는 기능에 체크(workflow 등)하고 Generate Token --> Token을 복사해서 저장해두기
- 토큰 컴퓨터에 저장하기 : Windows 자격 증명 관리자 --> Windows 자격 증명 --> git:https://github.com 자격 정보 생성(일반 자격 증명) --> Github 사용자명과 토큰 붙여넣기
  cf) 설정이 완료되면 자동적으로 SourceTree에도 등록되는 것을 확인 가능

<img width="638" alt="1" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/aa071485-f7e1-43cf-bc6a-e3829c080e97">
<img width="433" alt="2" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/47a31890-cd63-4e78-92c2-428967f93ac9">
<img width="505" alt="3" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/b0c3c3a3-02d7-4028-a4c6-b118983f2a1a">

<br> 

#### 5) Remote Repository(원격 저장소)
- Github에 Repository를 생성하고 Code를 누르고 나오는 HTTPS 주소를 복사

<img width="670" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/80947f8b-a2c9-4f49-8ace-25c22d53d97c">

<br>

- 로컬 저장소(git init으로 생성)에서 bash를 열고 아래의 명령어를 통해 Github Repository와 연결 
```
git remote add origin (원격 저장소 주소) # 연결하는 명령어
```
```
git branch -M main                        # 기본 Branch 이름을 main으로 설정
git remote                                # 원격 목록 확인
git remote -v                             # 원격 목록 자세히 확인
git remote remove (origin 등 원격 이름)    # 원격 지우기
```

## Flask 실습
#### 1) flask로 만들어진 app.py를 실행

<img width="250" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/a4d4aa16-20d0-4e4d-a080-932bf9760f29">
<img width="700" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/4fe086ff-6244-4890-bc80-435d484b9f02">

<br> 

#### 2) 로컬 IP로 접속 시도
- 로컬 호스트(localhost)를 나타내는 특별한 IP 주소: **127.0.0.1**
- 외부에서 접근 불가, 가상 컴퓨터에서 접속을 시도하니 Error가 발생한 것을 확인할 수 있다
<img width="400" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/3c2b9cd0-6805-4280-8dde-b7647dcee6ea">
<img width="500" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/121f02ef-8220-4215-a3fe-8ddb9987e095">

<br>

#### 3) 다른 IP로 접속 시도
- 특정 네트워크 상의 다른 컴퓨터나 장치를 가리키는 IP 주소
- 로컬 네트워크에서 다른 기기에 있는 서버에 접속하는 경우 사용, 외부에서도 접근 가능
<img width="400" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/5a73b8d6-c74d-4cee-b975-c2eaf0d21174">
<img width="500" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/57ba098e-3ec0-4657-bf53-f4eda2b50fe4">

