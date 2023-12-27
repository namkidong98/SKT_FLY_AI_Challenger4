## 01. Encoding&Scaling.ipynb
- Label Encoding과 One-Hot Encoding에 대해 학습한다
- 5가지 Scaler의 종류와 특징에 대해 학습한다
- Scaling 이전과 이후의 데이터 분포의 변화를 시각화를 통해 확인한다
![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/8984fb76-b61a-4c16-90b8-8a300fefd298)
![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/59c7be25-0832-40a7-80aa-e0830e6c6738)

<br> 

## 02. SVC_유방암_데이터.ipynb
- Sklearn에서 제공하는 유방암 데이터를 로드하고 StandardScaler를 통해 스케일링한다
- SVC(Support Vector Classifier) 모델을 학습하여 유방암 여부를 예측한다(95% 정확도)
![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/f7873ce6-edd5-4b80-b52b-736cd943f815)

<br> 

## 03. SVR_펭귄_데이터.ipynb
- 사용하는 파일: penguins.csv
- 펭귄 데이터의 구조를 확인하고 수치형 데이터에 대해 StandardScaler로 스케일링을 한다
- 범주형 데이터는 One-Hot Encoding을 하고 상관계수 히트맵을 그린다
- SVR(Support Vector Regressor) 모델을 학습하여 부리의 길이(Culmen length)를 예측한다
- scaling의 영향을 상쇄한 mse, rmse를 구해 성능을 평가한다
![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/9b38f6b2-7fef-4a28-ac2d-0cb98781af1f)
![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/15b646a3-106f-415f-8d8d-10d3505933a8)

<br> 

## 04. Keras기초_당뇨병_데이터.ipynb
- 사용하는 파일: diabetes.csv
- 피마 인디언 당뇨병 데이터인 'diabetes.csv'를 로드하고 이상치를 확인한다
- 이상치는 평균값으로 대체하고 Keras로 Dense Layer를 쌓아 MLP 모델을 설계한다
- 학습 횟수에 따른 train_loss, val_loss, train_acc, val_acc를 시각화한다
![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/445b9ac1-a438-4d5c-9b8c-5dcb027cb19c)

<br>

## 05. Keras기초_당뇨병_데이터.ipynb
- 사용하는 파일: spam.csv, spam.jpg
