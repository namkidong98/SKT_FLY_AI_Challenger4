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

## 05. Spam_Classification.ipynb
- 사용하는 파일: spam.csv, spam.jpg
- 스팸 메일 여부와 메일 내용으로 이루어진 'spam.csv'를 로드한다
- 전처리 과정: 알파벳 이외의 단어 제거, 소문자 변환, 토큰화(word_tokenize), 불용어(stopwords) 처리, 어간화(Stemming)
- TfidfVectorizer로 텍스트 데이터를 TF-IDF 행렬로 변환   
  cf) TF-IDF: "Term Frequency-Inverse Document Frequency"의 약자, 문서에서 어떤 단어가 얼마나 중요한지를 나타내는 통계적인 척도
-  DecisionTree, RandomForest 모델로 학습하고 spam 여부를 예측(정확도 98%)
![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/d704004e-1198-4488-aeee-8659750db642)

<br>

-  Spam인 메일의 텍스트 전체를 대상으로 WordCloud를 그려 어떤 어휘가 스팸 메일에서 자주 등장하는지 체크
![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/bae640de-b30a-408c-add1-2f69f2816d84)

