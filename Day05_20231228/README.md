## 01. Decision_Tree.ipynb
- Confusion Matrix에 대해 학습한다(정확도, 정밀도, 재현율, f1스코어)

![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/e066d9bc-7992-4c46-9c84-3561715a08b0)

- DecisionTree 모델에 대해 학습하고 하이퍼 파라미터(max_depth 등)에 대해 학습한다

![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/6016e771-f48e-4355-9b4d-1dc0561238ae)

<br> 

## 02. Penguins_DecisionTree.ipynb
- 사용하는 파일: penguins.csv
- 데이터의 구조를 파악하고 전처리, 스케일링을 진행한다
- Species를 Target으로 하여 DecisionTree 모델을 학습하여 예측한다(96% 정확도)

![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/0d69bb2f-1bf3-43dc-bd6b-13b9da864b3b)

![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/a813e17d-f2c1-418d-baaa-b4385fc837c6)

<br> 

## 03. Ensemble.ipynb
- Ensemble에 사용되는 Voting과 Bagging에 대해 학습한다
- Voting: 여러 개의 분류기(Classifier)를 사용하여 각각의 분류기 결과를 투표하여 예측
- Hard Voting : 각각 분류기의 결과값 중 가장 많은 것을 따른다   
   cf) 성능이 높은 분류기만 선택되고 나머지는 배제되는 문제가 발생
- Soft Voting : 분류기의 확률을 더하고 각각 평균을 내서 확률이 제일 높은 값으로 결과값을 선정

![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/a9adc998-5534-4f52-9c26-c2da7dd4ac77)

<br>

- voting과 다르게 서로 같은 알고리즘의 분류기를 조합   
   cf) RandomForest는 DecisionTree를 bagging으로 조합한 모델이다
![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/a91e149d-9f54-4165-a710-e2c24de52fff)

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
<img width="244" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/55dcbeca-4310-46b2-ab78-ec1e29bd2d48">


<br> 

## 04. Ensemble_Boston.ipynb


<br> 

## 05. MNIST_Keras.ipynb


<br> 

## 06. Shape_Classification.ipynb


<br> 

## 07. CIFAR10_Keras.ipynb


<br> 
