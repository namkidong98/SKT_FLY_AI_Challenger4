## VPN
- VPN(Virtual Private NetworK)는 인터넷 사에서 둘 이상의 네트워크를 안전하게 연결하기 위해 가상의 터널(VPN 터널)을 만들어 암호화된 데이터 전송이 가능한 네트워크
- VPN은 공용 IP 주소를 할당받아 인터넷에 연결하는 부분
- VPN Gateway : Gateway Subnet이라는 서브넷에 배포되는 2개 이상의 가상머신으로 이 VM에서 라우팅 테이블을 포함하여 관련 서비스를 실행
- VPN Gateway를 사용하여 두 가상 네트워크 간에 VPN 연결 설정
- vNet Perring, VPN Gateway : 사용자 지정하여 VNet을 연결
- P2S VPN : 개별 클라이언트에서 Azure 가상 네트워크와 연결
- S2S VPN : Azure VNet과 On-Premise를 연결

<br>

## Azure Load Balancer(부하 분산장치)
- Load Balancer(L4) : 애플리케이션 또는 서버 엔드 포인트에 대한 인바운드 및 아웃바운드 연결 및 요청 분산
- Application Gateway(L7) : 웹 애플리케이션 방화벽을 사용하여 보안을 가오하하면서 애플리케이션 서버 트래픽 분산 처리
- Traffic Manager : 고가용성 및 응답성을 제공, 글로벌 Azure 지역 전반의 서비스에 트래픽을 최적으로 분산

<br>

## 실습 - 내부 부하분산 장치 생성
- Load balancing 네트워크 트래픽을 효율적으로 여러 서버에 분산시켜 응답시간을 최소화하고 단일 리소스의 과부하를 방지하는 것
1. 가상 네트워크와 서브넷 만들기
2. 백엔드풀로 사용할 가상머신 만들기(2대의 Linux VM)
3. 부하 분산 장치 검색, 만들기
4. 백엔드풀, 상태 프로브, 부하분산 규칙, 인바인드 NAT 규칙 설정

<br>

## 1. 가상 네트워크 만들기
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/f039efc0-5247-4c94-9372-35e49e5ecdfc">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/a932b20c-abfb-42c4-bebe-42016e7f5c23">

- IP주소에서 default 날리고 두 개의 서브넷을 생성한다
- 첫 번째 서브넷은 Front로 10.0.2.0으로 시작주소를 설정하고 두 번째 서브넷은 Back으로 10.0.3.0을 시작주소로 설정한다

<img width="750" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/5bddd772-7881-49b6-9a43-d31e6cb1caca">

- 완성된 후 서브넷에 들어가보면 2개가 제대로 생성되어 있는 것을 확인할 수 있다

<br>

## 2. 백엔드풀로 사용할 가상머신 만들기

<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/68524f3b-9417-4b6e-8ad3-2ac5dc57485c">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/906bb7fc-c078-489a-bdcc-c4a5e85b5009">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/4918b514-5acd-44be-9f1f-06b8698524ea">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/3c98f799-c63e-474b-9738-84e93ba6e8bd">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/ef2bbaad-5c4d-406b-acab-fc79736c92aa">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/4fee80f9-3333-45ba-b7ff-664e7fbc1845">

- OS 디스크 유형을 '표준 SSD'로 바꾸어주고 서브넷을 Back(Front 말고)으로 연결해주어야 한다
- 부하분산을 'Azure Load Balancer'로 해야하지만 일부러 선택하지 않고 이후 Back에서 작업할 예정이다
- 부트 진단은 '사용 안함'으로 바꾸어주고 가상 머신을 만든다
- 2번째 서브넷에 대해서도 새로운 ssh key와 공용 IP를 새롭게 생성하고 동일하게 만든다 

<br>

## 3. 부하 분산 장치 검색, 만들기
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/65950655-25bf-483c-b3b2-9746003f5b1d">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/61afb0ae-4eb5-4969-a5ea-b6ba943ac267">

- 형식을 '공개'로 하면 Front 쪽에 붙인다는 것이다. Back에 붙이기 때문에 '내부'를 선택한다 --> 내부 부하분산 장치를 만드는 것이다

<br>

<img width="850" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/2a941b4b-a96b-4503-bee5-b5f854da7c54">
<img width="850" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/5151d030-e346-4e91-8702-ee6a4c225c51">

- 서브넷을 back으로 연결하고 할당을 '정적'으로 해서 IP 주소를 영구적으로 동일한 것을 사용하겠다는 것이다
- 잘 만들어졌다면 위와 같이 나타날 것이다

## 4. 백엔드풀, 상태 프로브, 부하분산 규칙, 인바인드 NAT 규칙 설정
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/fe8393cf-5c43-471e-926e-52a84a97af4c">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/e2f12cf9-608d-4ccc-ada3-ce87d2733a99">

- 부하 분산 장치에서 백엔드풀에 들어가서 추가에서 기존에 만들어 둔 두 개의 가상머신을 추가한 후 저장하고 나온다

<br>

<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/a7db6e07-b2bd-412f-b0e1-e1a47644c278">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/be71f97f-a76c-42b4-9605-123f135f6e5b">

- 다음으로 상태 프로브에 들어가서 backendlb1HttpProbe로 하나 만들어서 저장하고 나온다
- 다음으로 부하분산 규칙에 추가에 들어가서 프런트 엔드 IP주소, 백 엔드 풀, 상태 프로브 만든 것으로 선택해주고 포트, 백엔드 포트 80으로 설정하여 저장한다

<br>

<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/88b8addc-7f45-464a-85d4-999f82b5a6f6">
<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/cb3785c8-2b36-4adf-bf7c-7cd950f948aa">

- 마지막으로 인바운드 NAT 규칙 추가에 들어가서 위의 사진과 같이 설정한다
- 백엔드 풀의 현재 컴퓨터 수가 2인 이유는 backend에 연결된 가상 머신이 2개이기 때문이며, backend port를 22로 한 것은 linux machine이기 떄문이다
- 설정을 마춘 이후 '개요'로 돌아가면 아까는 비어있던 부분들이 다 채워진 것을 확인할 수 있다

<br>

## 저장소 만들기
<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/ca856136-874f-44c9-a9e9-8056ed4d8be6">
<img width="450" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/e5a59c42-bf06-4fcb-acac-4ef4f1c16134">

- 스토리지 계정을 만들고 그 안에 컨테이너를 생성한다
