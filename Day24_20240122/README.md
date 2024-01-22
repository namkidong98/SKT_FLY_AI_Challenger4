# Pytorch

## Pytorch 개요
- Pytorch : 2017년 초에 공개된 딥러닝 프레임워크, Lua언어로 개발되었던 Torch를 페이스북에서 파이썬 버전으로 내놓은 것
- Torch : 파이썬의 Numpy처럼 과학 연산을 위한 라이브러리로 공개, 이후 발전을 거듭하면서 딥러닝 프레임워크로 발전

<br>

## Pytorch의 특징 및 장점
- GPU, 텐서, 동적 신경망

- GPU(Graphics Processing Unit) : 연산 속도를 빠르게 하는 역할
  - 딥러닝에서는 기울기를 계산할 때 미분을 쓰는데, GPU를 사용하면 빠른 계산이 가능
  - 내부적으로는 CUDA, cuDNN이라는 API를 통해 GPU를 연산에 사용한다 
- 텐서(Tensor) : pytorch의 데이터 형태, 단일 데이터 형식으로 된 자료들의 다차원 행렬
  - Tensor는 간단한 명령어(변수 뒤에 .cuda()를 추가)를 사용해서 GPU로 연산을 수행하게 할 수 있다
- 동적 신경망 : 훈련을 반복할 때마다 네트워크 변경이 가능한 신경망
  - 학습 중에 은닉층을 추가하거나 제거하는 등 모델의 네트워크 조작이 가능하다
  - Tensorflow는 중간 중간 네트워크 조작이 불가능하며 디버깅도 어렵다

<br>

## Pytorch Architecture
<img width="700" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/1e2943f2-35d5-4602-b421-6a576606b4bc">

- Pytorch는 3개의 계층으로 구성되어 있다
  1. Pytorch API : 상위 계층, 사용자 인터페이스 제공, 실제 계산은 하지 않음
  2. Pytorch Engine : C++로 작성되었으며 다차원 텐서 및 자동 미분 처리
  3. 연산처리 : 가장 아래 계층, 텐서에 대한 연산을 처리


# Anaconda

## 가상환경 설정

<img width="600" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/f87de541-61ca-45fd-803b-4fcd5b3eedb8">
<img width="600" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/0b655448-5551-45ab-8f9a-ac878e1f442e">

```
conda create -n torch_book python=3.9.0    # 가상환경 생성
conda env list        # 가상 환경 목록 확인
activate torch_book   # 가상 환경 활성화
# conda env remove -n torch_book    # 가상 환경을 삭제할 경우
```

- Anaconda를 설치한 후, 'Anaconda Prompt'를 실행하고 위의 명령어들을 실행하여 가상환경을 설정한다
- 파이썬 3.10 이상을 설치하면 파이토치와 호환성 문제가 있기 때문에 3.9 버전을 설치한다
- 기본적으로 base가 있는 것을 확인할 수 있으며, 설치한 가상환경이 활성화되면 앞부분의 괄호가 바뀌는 것을 확인할 수 있다 

<br>

<img width="900" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/f31fe1d1-47fc-4022-bb2d-dbb64184e1d4">


```
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia  # pytorch 설치
pip install jupyter notebook    # 주피터 노트북 설
jupyter notebook                # 주피터 노트북 실행
```

<br>

<img width="723" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/798b4c48-9dfd-47f4-a7dc-fa34f49501c8">

```python
import torch

# GPU 정보 출력
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("사용 중인 디바이스:", device)
```

- conda로 가상 환경을 생성하고 torch를 설치한 이후 vscode로 들어가서 kernel에서 해당 가상 환경을 골라준다
- 위의 명령어를 실행했을 때 cpu가 아니라 cuda가 출력되면, 컴퓨터의 내장 GPU를 사용할 수 있는 상태가 된 것이다
