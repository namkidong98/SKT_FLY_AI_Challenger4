### 이미지 관련 분야
1. Image Classification
2. Image Detection
3. Image Segmentation

# 이미지 분류를 위한 신경망
- 채널 수는 늘리고 feature map은 줄이는 방향으로 나아간다
- 귀, 코 등을 세부하게 보도록 feature map의 크기는 줄어들고 귀, 코 등 다양한 특징에 대해 보니 채널 수는 늘어나야 하는 것이다

## LeNet-5
<img width="800" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/9b5c192f-a096-431b-bc20-b32bc724f663">
<img width="600" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/ab724122-9cb9-4513-8b70-f69119748563">

## AlexNet
<img width="800" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/4b043ae7-5eae-4c4b-80cc-243c8cb84332">
<img width="600" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/907b4e39-6f9b-4d3b-bd05-97f284ae866f">

## VGGNet
<img width="800" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/f7d808f1-4f94-4573-853d-bc1957ffa781">
<img width="600" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/3f9b1e3a-b068-423b-a563-55ad50298db5">
<img width="600" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/3c7558ee-d820-4f14-9669-6f718369e2ba">
<img width="600" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/43ae3f2e-28bc-4300-824a-f7cb66ae71dd">

 - 3x3 필터와 padding=1을 사용해서 이미지 크기는 유지하고 채널만 늘리다가, max_pooling으로 줄인다
 - 기존의 AlexNet보다 훨씬 깊게 만들었다는 특징이 있다

