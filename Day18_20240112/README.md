## Kubernetes Architecture

<img width="700" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/c0876b0f-e845-4879-94ef-31459315ba75">

<br>

## Minikube
### 1. Prerequisite
- References : <a href='https://minikube.sigs.k8s.io/docs/start/'>minikube</a>, <a href='https://kubernetes.io/ko/docs/tasks/tools/install-kubectl-linux/'>kubectl</a>
- 최소 사양 : CPU(2 이상), Memory(2GB 이상), Disk(20GB 이상), 가상화 tool(Docker, Hyperkit, Hyper-V, ...) 

<br>

### 2. Install Minikube
<img width="750" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/35f63020-0eec-450f-988f-eddbef6906cc">

```
curl -LO https://storage.googleapis.com/minikube/releases/v1.22.0/minikube-linux-amd64 # 최신 버전의 바이너리 다운

sudo install minikube-linux-amd64 /usr/local/bin/minikube  # 설치 시작 

minikube --help  # 실행 되면 minikube가 제대로 설치된 것
```
- AMD 기반의 CPU를 기준으로 minikube의 최신 버전(v1.22.0) 바이너리를 다운 받고 실행할 수 있도록 변경한다
- ARM 기반의 CPU는 공식 문서를 확인해야 한다

<br>

### 3. Install Kubectl
- Kubectl : Kubernetes Cluster(server)에 요청을 간편하게 보내기 위해서 널리 사용되는 client tool

<img width="750" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/266c0370-c099-459d-803f-ff881591bd30">

```
curl -LO https://dl.k8s.io/release/v1.22.1/bin/linux/amd64/kubectl   # kubectl 최신 버전(v1.22.1)의 바이너리 다운

sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl  # root 권한으로, 나머지는 755권한으로 kubectl을 설치

kubectl --help  # 실행되면 kubectl가 제대로 설치된 것 
```

<br>

### 4. Start Minikube

<img width="750" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/7f3c82b5-37da-4eea-bd26-5d42ea14fbf1">

```
minikube start --driver=docker  # minikube를 docker driver 기반으로 시작
```

- 이렇게 해서 만약 오류가 난다면 아래와 같이 시도해볼 수 있다

<img width="750" alt="image" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/16825975-0b4a-4b44-85df-6c0af3a41e79">

```
sudo usermod -aG docker $USER  # 현재 사용자를 docker 그룹에 추가하여 Docker 명령어를 실행할 권한을 제공
newgrp docker                  # 현재 세션을 새로운 그룹 세션으로 전환하여 사용자가 새로운 그룹의 권한을 즉시 사용할 수 있도록
minikube start --driver=docker    
```

- 위의 명령어를 추가하고 다시 minikube를 시작하면 제대로 동작한다


## YAML


