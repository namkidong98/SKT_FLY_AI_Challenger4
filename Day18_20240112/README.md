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

<br>

<img width="750" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/7193dc6a-2791-4d83-98a7-dbd9fdbec7b4">

```
minikube status                  # 정상적으로 생성 되었는지 상태를 확인

kubectl get pod -n kube-system   # minikube 내부의 default pod들이 정상적으로 생성되었는지 확인
```

### 5. Delete Minikube
<img width="750" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/53a8790b-b2d2-452a-b72a-f476d233ffe1">

- 위의 명령어를 실행하여 minikube를 삭제할 수 있다
- "Removed all traces of the "minikube" cluster" 가 출력되어야 잘 삭제된 것이다

<br>

## Pod

### 1. Pod yaml 작성 및 Pod 생성
<img width="750" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/48656c87-361d-4d2d-9bd1-4634bd29bedd">

```yaml
apiVersion: v1 
kind: Pod 
metadata:  
  name: counter 
spec: 
  containers: 
  - name: count 
    image: busybox 
    args: [/bin/sh, -c, 'i=0; while true; do echo "$i: $(date)"; i=$((i+1)); sleep 1; done'] 
```

```
vi pod.yaml                 # pod.yaml을 vim을 열어서 작성한다

kubectl apply -f pod.yaml   # yaml에 해당하는 kubernetes resource를 생성 또는 변경
                            # -f : 파일 참조 옵션

kubectl get pod             # 생성한 Pod의 상태를 확인
```

- kubernetes resource 의 desired state 를 기록해놓기 위해 항상 YAML 파일을 저장하고, 버전 관리하는 것을 권장한다
- kubectl run 명령어로 YAML 파일 생성 없이 pod 을 생성할 수도 있지만, 이는 kubernetes 에서 권장하는 방식이 아니므로 생략한다
- 시간이 지난 후 Running 으로 변하는 것을 확인할 수 있다

<br>

### 2. Pod 조회

```
kubectl get pod # 

kubectl get pod -A # # 모든 namespace 의 pod 을 조회

kubectl get pod <pod-name> # pod 하나를 조금 더 자세히 조회하는 명령어

kubectl describe pod <pod-name>  

kubectl get pod -o wide # pod 목록을 보다 자세히 출력

kubectl get pod <pod-name> -o yaml

kubectl get pod -w   # kubectl get pod 의 결과를 계속 보여주며, 변화가 있을 때만 업데이트

```
