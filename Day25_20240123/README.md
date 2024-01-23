### 이미지 관련 분야
1. Image Classification
2. Image Detection
3. Image Segmentation

# 이미지 분류를 위한 신경망
- 일반적으로 채널 수는 늘리고 feature map은 줄이는 방향으로 나아간다
- 귀, 코 등을 세부하게 보도록 feature map의 크기는 줄어들고 귀, 코 등 다양한 특징에 대해 보니 채널 수는 늘어나야 하는 것이다

<br>

## LeNet-5
<img width="800" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/9b5c192f-a096-431b-bc20-b32bc724f663">
<img width="600" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/ab724122-9cb9-4513-8b70-f69119748563">

- 합성곱(Convolution)과 다운 샘플링(Sub-sampling)을 반복적으로 거치면서 마지막에 완전연결층에서 분류를 수행
- 예측력이 좋지 않은데, 극히 일부의 데이터(500개)를 이용해서 모델 학습을 진행했기 때문이다

<br><br>

## AlexNet
<img width="800" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/4b043ae7-5eae-4c4b-80cc-243c8cb84332">
<img width="600" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/907b4e39-6f9b-4d3b-bd05-97f284ae866f">

- ImageNet 영상 데이터 베이스를 기반으로 한 화상 인식 대회인 ILSVRC 2012에서 우승한 CNN 구조
- AlexNet은 합성곱층 5개와 완전 연결층 3개로 구성되어 있으며 마지막 완전연결층은 1000개를 분류하기 위해 softmax 활성화 함수를 사용하고 있다
- 전체적으로 보면 GPU 2개를 기반으로 한 병렬 구조인 점을 제외하면 LeNet과 크게 다르지 않는다
- AdaptiveAvgPool2d는 AvgPool2d와 유사하지만 AvgPool2d가 아래 공식에 맞게 커널 사이즈, 스트라이드 크기를 정의해야 하는 반면, AdaptiveAvgPool2d는 출력 크기를 지정함으로써 Pooling을 진행하는 것이다

<img width="400" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/3c1b0d7e-57a8-4369-8304-bc00e4104e16">

<br><br>

## VGGNet
<img width="800" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/f7d808f1-4f94-4573-853d-bc1957ffa781">
<img width="600" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/3f9b1e3a-b068-423b-a563-55ad50298db5">
<img width="600" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/3c7558ee-d820-4f14-9669-6f718369e2ba">
<img width="600" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/43ae3f2e-28bc-4300-824a-f7cb66ae71dd">

- VGGNet은 합성곱층의 파라미터 수를 줄이고 훈련 시간을 개선하려고 탄생했다
- 즉, 네트워크를 깊게 만드는 것이 성능에 어떤 영향을 미치는지 확인하고자 나온 것이다
- 따라서 VGG 연구팀은 깊이의 영향만 최대한 확인하고자 합성곱층에서 사용하는 필터/커널의 크기를 가장 작은 3x3으로 고정했
- 3x3 필터와 padding=1을 사용해서 이미지 크기는 유지하고 채널만 늘리다가, max_pooling으로 줄인다
- 기존의 AlexNet보다 훨씬 깊게 만들었다는 특징이 있다고 볼 수 있다

<br>
