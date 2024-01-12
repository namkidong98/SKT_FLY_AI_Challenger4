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

### 1. Pod이란
- Pod : Kubernetes에서 생성하고 관리할 수 있는 배포 가능한 가장 작은 컴퓨팅 단위
- Kubernetes는 Pod 단위로 scheduling, load balancing, scaling 등의 관리 작업을 수행한다
- Pod는 Container를 감싼 개념이라고 생각할 수 있다
- 하나의 Pod 은 한 개의 Container 혹은 여러 개의 Container 로 이루어져있을 수 있다 
- Pod은 내부의 여러 Container 는 자원을 공유한다
- Pod은 Stateless한 특징을 지니고 있으며, 언제든지 삭제될 수 있는 자원이다

<br>

### 2. Pod yaml 작성 및 Pod 생성
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

### 3. Pod 조회

<img width="900" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/e841fcf5-8060-4189-8aeb-1b2f7441f821">

```
kubectl get pod               # 기본적인 pod 조회

kubectl get pod -A            # 모든 namespace 의 pod 을 조회

kubectl get pod -o wide       # pod 목록을 보다 자세히 출력

kubectl get pod -w            # kubectl get pod 의 결과를 계속 보여주며, 변화가 있을 때만 업데이트

kubectl get pod <pod-name>    # pod 하나를 조금 더 자세히 조회하는 명령어

kubectl get pod <pod-name> -o yaml  # yaml 형식으로 출력

kubectl describe pod <pod-name>  
```

### 4. Pod 로그

<img width="500" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/d7219945-a8c0-4c70-a975-f5a857dc5bd9">

```
## Pod 안에 하나의 Container만 있는 경우
kubectl logs <pod-name>     # Pod의 로그를 확인

kubectl logs <pod-name> -f  # Pod의 로그를 계속 보여 (Ctrl + C로 중단)

## Pod 안에 여러 개의 Container가 있는 경우
kubectl logs <pod-name> -c <container-name> 

kubectl logs <pod-name> -c <container-name> -f 
```

### 5. Pod 내부 접속

<img width="640" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/b88eda02-4349-41a5-be2e-a4be8d52d077">

```
kubectl exec -it <pod-name> -- <명령어>  # Pod 내부에 접속

# Pod 안에 여러 개의 Container가 있는 경우
kubectl exec -it <pod-name> -c <container-name> -- <명령어> 
 
```

### 6. Pod 삭제

<img width="515" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/482e664a-8274-4387-bd83-d874dcb8d060">

```
kubectl delete pod <pod-name>     # 해당 이름의 Pod를 삭제

kubectl delete -f <YAML-파일-경로> # 리소스를 생성할 때, 사용한 YAML 파일을 사용해서 삭제
```

<br><br>

## Deployment

### 1. Deployment란
Deployment(디플로이먼트)는 Pod와 Replicaset에 대한 관리를 제공하는 단위입니다.  

https://kubernetes.io/ko/docs/concepts/workloads/controllers/deployment/ 

관리라는 의미는 Self-healing, Scaling, Rollout(무중단 업데이트) 과 같은 기능을 포함합니다. 

조금 어렵다면 Deployment 는 Pod을 감싼 개념이라고 생각할 수 있습니다.  

Pod 을 Deployment 로 배포함으로써 여러 개로 복제된 Pod, 여러 버전의 Pod 을 안전하게 관리할 수 있습니다. 

Deployment 의 자세한 구조는 생략하겠습니다. 

<br>

### 2. Deployment 생성

<img width="750" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/db74b7ea-8645-4969-93da-948b13f261bc">

```yaml
apiVersion: apps/v1     # kubernetes resource 의 API Version 
kind: Deployment        # kubernetes resource name 
metadata:               # 메타데이터 : name, namespace, labels, annotations 등을 포함 
  name: nginx-deployment 
  labels: 
    app: nginx 
spec:                   # 메인 파트 : resource 의 desired state 를 명시 
  replicas: 3           # 동일한 template 의 pod 을 3 개 복제본으로 생성합니다. 
  selector: 
    matchLabels: 
      app: nginx 
  template:             # Pod 의 template 을 의미합니다. 
    metadata: 
      labels: 
        app: nginx 
    spec: 
      containers: 
      - name: nginx         # container 의 이름 
        image: nginx:1.14.2 # container 의 image 
        ports: 
        - containerPort: 80 # container 의 내부 Port 
```
```
vi deployment.yaml                # deployment 생성을 위한 yaml 파일 생성
kubectl apply -f deployment.yaml  # 해당 yaml 파일로 deployment 생성
```
- replicas를 3으로 설정해서 pod이 3개가 ContainerCreating에서 Running으로 변화하는 것도 확인할 수 있다

<br>

### 3. Deployment 조회

<img width="750" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/910d3f92-a100-4883-ba44-c0ac38067f88">

```
kubectl get deployment      # 생성한 Deployment의 상태를 확인

kubectl get deployment,pod  # Deployment와 관리되는 Pod들의 상태를 한번에 확인
                            # deployment와 pod 사이에 ,를 바로 넣어야 함. 띄어쓰기 있으면 오류 발생

kubectl describe pod <pod-name>
```
- pod 의 정보를 자세히 조회하면 Controlled By 로부터 Deployment 에 의해 생성되고 관리되고 있는 것을 확인할 수 있다

<br>

### 4. Deployment Auto-healing

<img width="850" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/6c6dbd2c-de1d-4bce-9b7f-a8a57a924771">

```
kubectl delete <pod-name>  # 해당 이름의 pod를 삭제

kubectl get pod # 현재 pod의 상태 확인
```
- 기존에 deployment의 control을 받던 k6j85을 삭제했다
- kubectl get pod를 하면 여전히 pod이 3개인 것을 확인할 수 있다
- 대신 k6j85는 삭제된 것이 맞고 대신 rvt92이 생성되어 auto-healing된 것을 확인할 수 있다 

<br>

### 5. Deployment Scaling

<img width="750" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/f3a2b01e-d070-4325-bb4a-9a6fed52cf51">

```
kubectl scale deployment/nginx-deployment --replicas=5 

kubectl get deployment,pod 
```
- replica 개수를 위의 코드를 통해 늘릴 수 있다

```
kubectl scale deployment/nginx-deployment --replicas=1 
 
kubectl get deployment,pod
```
- 위의 코드로는 replica 개수를 줄일 수 있다

<br>

### 6. Deployment 삭제

<img width="750" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/2fd72689-fa6f-4742-ab30-3add206eee40">

```
kubectl delete deployment <deployment-name> # deployment를 직접 삭제
kubectl delete -f <YAML-파일-경로>           # yaml 파일로 생성시킨 deployment를 삭제

kubectl get deployment # 현재 Deployment 상태 확인             
kubectl get pod        # 현재 Pod 상태 확인
```
- Deployment 의 Control 을 받던 pod 역시 모두 삭제된 것을 확인할 수 있다

<br><br>



