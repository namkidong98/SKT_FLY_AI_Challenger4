## 부하 분산 장치(L4) 구성 요소

<img width="626" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/dab3f064-2d0f-4bdf-b874-b2d443808d67">

1. 백엔드 풀 : 들어오는 요청에 대해 처리할 가상 머신 세트를 지정
2. 상태 프로브 : 백 엔드 풀의 가상 머신 상태 모니터링
3. 부하 분산 규칙 : 백 엔드 풀의 가상 머신에 트래픽 분산시키는 방법 정의
4. 인바운드 NAT : 프론트 엔드 IP와 포트 번호의 조합으로 들어오는 트래픽을 해시기반 분산 처리를 통해 백엔드 풀의 특정 VM으로 전달

<br>

# Azure Application Gateway(L7)
<img width='700' src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/420fd31e-2a18-4d94-9392-f28ca2690ce7">

- Azure APplication Gateway : 웹 애플리케이션에 대한 트래픽을 관리할 수 있도록 하는 웹 트래픽 부하 분산 장치
- URL이 customers가 들어오는 URL에 있는 경우 customers에 대해 구성된 서버(풀이라고도 함)로 라우팅
- 만일 video일 경우 해당 트래픽은 video에 대해 구성된 서버(풀)로 라우팅

<br>

## L7 구성

<img width='700' src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/8e3072ef-fb2b-4baa-b69e-99394b34182e">

- 요청 URL에 있는 호스트 이름, 포트 및 경로를 기반으로 트래픽을 웹 서버풀로 라우팅
- 웹 서버는 Azure 가상 머신, Azure 가상머신 확장 집합, Azure App Service로 구성

<br>

## L7 생성
1. 가상 네트워크와 서브넷 만들기
2. 백엔드 풀로 사용할 가상머신 만들기(2대의 Windows VM)
3. Application Gateway를 위한 전용 서브넷 추가
4. Application Gateway 만들기
5. 만들어진 Application GateWay 테스팅

<br>

## 1. 가상 네트워크와 서브넷 만들기
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/9889afcf-ef31-4321-8af7-b8d5da1820e6">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/8a9b0a11-1873-4c90-8501-f0abfff109f2">

## 2. 백엔드 풀로 사용할 가상머신 만들기(2대의 Windows VM)
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/ef390c58-fe49-44e6-88f5-9f6216bf2002">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/f644b012-6f04-47fd-9fcc-74fe76476c5a">

- Windows 10은 라이선싱을 선택해야 배포가 되고 Server는 라이선싱을 선택하지 않아도 된다

<br>

<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/ccc45e66-7130-4c08-81c9-82faa60c7ce7">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/afbb5191-3f3d-4326-825e-fdfae86a2254">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/321f6a02-e4c0-4fa5-91ad-b97249d82d9a">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/3fca12a1-3c2b-4076-8ca1-be5e8dbc1991">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/37f70b4a-09f4-43f8-92b8-5ea47cf7e402">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/ca63cd8d-ec57-47ca-ae94-f13e3ddd7f07">

- 동일한 방식으로 2개의 VM을 만든다

<br>

### 가상 머신 접속해서 Default.htm 설정
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/73ff59a2-8882-46a2-acec-ef5db1e8154b">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/8787dc92-da38-442e-ab8d-07c92a757839">

- 가상머신 - 연결로 가서 RDP를 다운로드 받고, 가상 머신에 접속해서 Windows PowerShell ISE에서 "Install-WindowsFeature -Name Web-Server -IncludeManagementTools를 실행
- Windows(C)-inetpub-wwwroot에 Default.htm을 생성하고 기존 컴퓨터에서 공용 IP주소로 접속하면 랜더링해서 위와 같이 보여주게 된다

<br>

## 3. Application Gateway를 위한 전용 서브넷 추가
<img width="750" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/7066eec0-a428-4cce-a9d2-4a2c7ff08c66">

<br><br>

## 4. Application Gateway 만들기
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/28d2430a-7c27-496c-8379-1f2f33ca31e4">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/c187d752-2db4-4c3a-88bf-56ccae44e710">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/150eac4f-9eb0-49dd-bdb9-6436ec7323e0">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/61427018-9dfa-4778-95eb-bfb22e116c50">

- agw : application gateway / pip : public ip

<br>

<img width="900" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/80937706-06ea-49de-a1bc-a38500f85847">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/ea697cd5-700e-40fd-81fe-7883d7a0f99f">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/e86d1ba7-a0e9-473c-88f2-0902c8bc0081">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/5363a9a3-5349-42cf-9145-51e6be36b1bb">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/fe9ecf6a-d937-418a-9643-c879ea7994f6">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/8b28bf1c-15f5-4181-b8d8-a8fc30901c98">

<br><br>

### 가상 머신 비활성화 --> 프라이빗 IP만 열게 만들기
<img width="937" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/5ea17d19-9457-4dbc-a705-3530ba48cd47">
<img width="818" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/a6d9ce46-bdb3-4de5-8dd1-dd54282a3284">

- 가상 머신의 네트워킹에 들어가서 인터페이스 안에서 IP구성에서 정적으로 바꾸고 비활성화를 한다
- 비활성화를 하고 나면 공용 IP 칸이 비워지는 것을 확인해야 한다

<br><br>

## 5. 만들어진 Application GateWay 테스팅
<img width="300" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/7269c82c-dd57-4c4c-a103-9b50a30096c6">
<img width="300" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/b238a361-beea-4bb7-9055-16ac1dbac978">

- Gateway의 공용 IP로 여러번 접속을 시도하면 부하 분산이 되는 것을 확인할 수 있다

<img width="428" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/38a3814b-db56-45fd-87b9-93e1294f758d">

```
$az group delete --name 리소스그룹 --no-wait --yes
```

- Application Gateway 포함 리소스 그룹 삭제하기

<br><br>

# 가상 머신 확장 집합(VMSS)
<img width='700' src='https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/7c868cec-182e-4de2-9dd2-d897268f239a'>

- 가상 머신 확장 집합(VMSS : Virtual Machine Scale Sets) : 부하 분산된 VM 그룹을 생성하고 관리 가능
- VMSS는 Azure Portal에서 VM을 생성한 것과 다르게 VM을 정의된 일정이나 요구사항에 따라서 자동의 생성하거나 제거할 수 있음
- 장점 : 다수 VM 생성 및 관리의 단순화, 고가용성 및 애플리케이션 복원력 제공, 리소스 수요 변화에 따라 자동으로 애플리케이션 크기 조정

<br>

## VMSS 생성
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/6bf807bf-fd6c-4115-b748-93ca49b2dddc">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/f1164c32-1301-4d2c-86a6-47ddb83c266d">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/80ed7f09-40a6-4419-b1fd-928b69069d26">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/5b58f47e-650e-4cc1-9566-4cce3ff7bcc8">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/3b5e6533-d8b0-441d-b9fc-73730295585e">
<img width="900" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/e1f8e985-9928-4629-807e-5722cdad8c30">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/d6e4e31e-3200-47a4-941c-3d3a9ae467a7">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/7392a6ab-2e86-4530-b3d5-65c5a82b873f">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/08848116-3ed4-45f3-9071-dcf147ca5715">

<br>

## VMSS  수동 크기 조정

<img width="900" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/f2c76f8e-55d1-48a9-94ea-cd2e1e98509d">
<img width="900" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/1afe8db4-0dfa-42e7-b576-03e79a47fcc1">
<img width="900" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/7d42b68d-a204-4a66-8897-3dad43e72ea1">

- 처음에는 인스턴스가 1개이다가 '확장 중'에서 2개로 늘리고 나니 인스턴스가 자동적으로 2개로 늘어난 것을 확인할 수 있다

<br>

<img width="900" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/a7bff1b9-c9fd-492e-818f-3636763ddbad">
<img width="900" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/b0218aa6-cb19-4498-8d19-e279956c3325">

- '확장 중'에서 다시 수동으로 인스턴스 수를 1로 줄이니 인스턴스가 자동적으로 1개 삭제된 것을 확인할 수 있다

<br>

# App Service


