## DevOps
- DevOps = Development(개발) + Operations(운영)
- MLOps = DevOps + Machine Learning의 느낌

<br>

<img width="500" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/481fa61f-e129-44ca-b088-73d90f19ca0f">


## 설치해야 하는 것들
- Ubuntu :

<img width="500" alt="2_Ubuntu" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/085af8bd-0d5d-4a85-be8f-368765fbd290">

- Git :
- SourceTree : Git을 GUI로 이용할 수 있게 해주는 Tool   
  cf) https://www.sourcetreeapp.com/

<img width="500" alt="2_sourcetree" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/fa7180fc-8d0c-45f2-9041-49d5c7c2c9fb">

- VS Code : Material Icon Theme, WSL extension 설치하기

## Hyper-V
- Microsoft Hyper-V : x64 시스템을 위한 하이퍼바이저 기반의 가상화 시스템, Windows Pro(Windows11)에서는 기본적으로 제공된다
- Windows 기능 켜기/끄기 안의 Hyper-V를 체크해준다

<img width="275" alt="1" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/40be9cea-4379-49e5-8f55-4879348a47ef">

- 재부팅 후 'Hyper-V 관리자'를 통해 설치한 Ubuntu iso를 사용하여 가상 머신을 설치한다

<br>

## Git
#### 1) Global 
- Git의 설정을 전역적으로 설정하는 명령어들을 사용한다
```
git config --global (명령어)
```

<img width="500" alt="4_git global" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/f0cd022d-8c11-4d47-a99f-8796034622f9">

#### 2) Local Repository
- VS Code에서 Explorer로 지정된 파일을 Open한 뒤, bash로 terminal을 연다
- 아래의 명령어를 입력하여 local repository를 생성한다
```
git init  # 로컬 저장소 만들기
```
<img width="500" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/d41a8c28-ca04-4342-9378-06c6d4aa7140">

<br>

- Material Icon Theme을 설치하면 파일 옆에 'U'라는 표시가 뜨고 add한 파일에는 'A'가 표시된다
- U (Untracked): Git 저장소에 아직 추적되지 않은(untracked) 파일
- A (Added):  Git 저장소에 새로 추가된(added) 파일

<img width="425" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/bd510687-17c9-4a63-a326-5867d3456bdc">
<img width="392" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/4c3dd6fa-f00b-4853-9c03-f636d0189a69">

