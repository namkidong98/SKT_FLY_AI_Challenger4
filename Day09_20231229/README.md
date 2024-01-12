## 01. Cats_Dogs_Classification.ipynb
- tensorflow_datasets에서 'cats_vs_dogs'를 로드한다
- 이미지의 크기를 150x150으로 정하고 정규화한다

![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/ebea117f-45e9-4ac2-b844-058a5fb0b59d)

-  tensorflow를 바탕으로 간단한 CNN모델을 설계하고 학습한다 (validation_accuracy: 85%)

![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/b9a90acf-664f-4e18-b549-76c84543c6cf)

<br> 

## 02. Cats_Dogs_전이학습.ipynb
- 1번 파일에서 사용했던 것과 동일하게 'cats_vs_dogs'를 토대로 전이학습(Transfer Learning)을 학습한다
- Resnet을 기반으로 마지막 fully connected layer만 교체한다
- 기존의 Resnet의 파라미터는 학습하지 않도록 설정한다
```python
from tensorflow.keras.applications import ResNet50
from tensorflow.keras import layers, models

# 사전 훈련된 ResNet50 모델 로드 (맨 위 레이어 제외)
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(150, 150, 3))

# 사전 훈련된 모델의 레이어를 동결
for layer in base_model.layers:
  layer.trainable = False

# 새로운 모델 생성 (사전 훈련된 모델 위에)
model = models.Sequential()
model.add(base_model)
model.add(layers.Flatten())
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(1, activation='sigmoid'))

# 모델 컴파일
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
```

<img width="332" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/23fefbe4-4e31-4ac7-974b-a5863b54f942">

- 제대로 학습이 되지 않는 것을 확인할 수 있는데(Validation_Accuracy:75%), Learning_rate를 낮출 필요가 있어 보인다

![image](https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/732180e3-cfaa-413c-adbd-9ed71211bdd5)

<br> 
