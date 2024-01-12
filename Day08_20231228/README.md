## 01. Decision_Tree.ipynb
- Confusion Matrix에 대해 학습한다(정확도, 정밀도, 재현율, f1스코어)

<img width="500" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/e066d9bc-7992-4c46-9c84-3561715a08b0">

- DecisionTree 모델에 대해 학습하고 하이퍼 파라미터(max_depth 등)에 대해 학습한다

<img width="500" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/6016e771-f48e-4355-9b4d-1dc0561238ae">

<br> 

## 02. Penguins_DecisionTree.ipynb
- 사용하는 파일: penguins.csv
- 데이터의 구조를 파악하고 전처리, 스케일링을 진행한다
- Species를 Target으로 하여 DecisionTree 모델을 학습하여 예측한다(96% 정확도)

<img width="500" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/0d69bb2f-1bf3-43dc-bd6b-13b9da864b3b">

<img width="500" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/a813e17d-f2c1-418d-baaa-b4385fc837c6">

<br> 

## 03. Ensemble.ipynb
- Ensemble에 사용되는 Voting과 Bagging에 대해 학습한다
- Voting: 여러 개의 분류기(Classifier)를 사용하여 각각의 분류기 결과를 투표하여 예측
- Hard Voting : 각각 분류기의 결과값 중 가장 많은 것을 따른다   
   cf) 성능이 높은 분류기만 선택되고 나머지는 배제되는 문제가 발생
- Soft Voting : 분류기의 확률을 더하고 각각 평균을 내서 확률이 제일 높은 값으로 결과값을 선정

<img width="500" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/a9adc998-5534-4f52-9c26-c2da7dd4ac77">

<br>

- voting과 다르게 서로 같은 알고리즘의 분류기를 조합   
   cf) RandomForest는 DecisionTree를 bagging으로 조합한 모델이다
<img width="500" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/a91e149d-9f54-4165-a710-e2c24de52fff">

<br>

- 유방암 데이터를 활용하여 LogisticRegression, KNN으로 예측하고 Voting을 통해 성능 향상을 확인한다
```python
classifiers = [lr_clf, knn_clf, vo_clf]
for classifier in classifiers:
  classifier.fit(X_train, y_train) # 각각의 모델에 대해 학습
  y_pred = classifier.predict(X_test)
  name = classifier.__class__.__name__
  print(f"{name} 정확도 : {accuracy_score(y_test, y_pred)}")
```
<img width="500" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/55dcbeca-4310-46b2-ab78-ec1e29bd2d48">


<br> 

## 04. Ensemble_Boston.ipynb
- 사용하는 파일: Boston_house.csv
- Boxplot을 통해 Outlier를 확인하고 전체 데이터에서 각 Column별 이상치 데이터의 개수를 출력한다

<img width="800" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/5eb8f1f2-3b38-4e11-bcea-f5eaa56f0aa7">

- MinMaxScaler로 스케일링을 하고 regplot을 통해 각각의 Column과 target 사이의 상관성을 시각화한다

<img width="800" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/d8014edb-3d59-4823-946d-de6ed81a1499">

- 상관계수를 히트맵으로 시각화한 것과 비교하면 확실히 Target과 상관계수가 높은 Column일수록 추세선의 기울기가 가파른 것을 확인할 수 있다

<img width="500" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/c2e2a93e-f822-4aac-9f79-0d54811744b3">


<br> 

## 05. MNIST_Keras.ipynb
- 딥러닝 순서 : 데이터셋 업로드 --> 데이터 전처리 --> 모델 구성 --> 모델 컴파일 --> 모델 훈련 --> 정확성 평가

#### 1) MNIST 
- MNIST 데이터셋을 로드하여 각각의 숫자 이미지가 어떻게 텐서로 표현되는지 시각화해본다
```python
import numpy as np
np.set_printoptions(linewidth=200) # 출력 결과의 너비를 늘리는 부분

for i in range(2):
  for j in range(28):
    for k in range(28):
      value = x_train[i][j][k]
      formatted_value = "{:0.4f}".format(value)
      output = "0.0   " if value == 0 else formatted_value
      print(output, end=' ')
    print()
  print()
```

<img width="1108" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/b0660df9-aaa8-41a4-a34c-eda468e63126">

<img width="1107" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/141e1c0f-2cb2-4a7e-8e73-513698aec5c8">

- 간단한 Dense Layer를 쌓은 모델로 MNIST의 손글씨를 예측한다(정확도 99%)

#### 2) Fashion-MNIST 
- Fashion-MNIST 데이터셋을 로드하여 CNN 모델을 통해 학습하고 정확도를 체크한다(정확도 93%)

![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/00d99bf3-4c49-44a6-bde4-ae75b44badec)

<br> 

## 06. Shape_Classification.ipynb
- 사용하는 파일: shapes.zip
- shapes.zip을 압축 해제하여 나오는 circles, squares, triangles을 분류하는 모델을 설계한다

![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/7707cb8d-2f13-4ddb-81fd-182731ed43c4)

- CNN 모델을 사용하여 학습 및 예측을 진행한다(정확도 94%)

![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/c486e694-62f2-405b-828b-d1a703ccddbd)

<br> 

## 07. CIFAR10_Keras.ipynb
- CIFAR10 데이터셋을 로드하여 이미지를 정규화(255로 나누기)를 진행한다
- Dropout, BatchNormalization을 사용한 CNN 모델을 설계하고 학습 및 예측을 진행한다(정확도 81%)

![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/b0017892-be73-4848-ab5a-91c5bcecf757)

<br> 
