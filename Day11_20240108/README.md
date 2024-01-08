참고 링크 : https://github.com/nongaussian/class-2024-skt-fly-ai?tab=readme-ov-file

## Gradient Descent & Propagation
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/0c811734-2952-462b-85f7-f3f64a50c22b">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/42f52e62-61a4-49de-b668-7d2ff68b9320">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/9adaffe5-ae07-4e22-861b-ae16bc25ded2">
<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/208a200f-d495-4fe0-9877-022ee6bf6769">

<br><br>

## Markov Reward Process & Decision Process

<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/33267f3b-6122-4f18-a223-585f1f05b51b">

<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/f3507791-877d-4d5e-b236-923a6510c863">

<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/db8f578c-cd99-4dc4-a5d1-d33573bfc4be">

<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/e69020de-4233-44ae-81d6-9e7a1039c9cb">

<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/806125c2-b961-457b-8a21-3db8974e83fa">

<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/79bff584-da32-4931-bc6c-490d36dbeff1">

<br>

### Result of Two Practices   

<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/5e563ee7-aa1a-4509-874f-6f737797844a">

<img width="450" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/86eedcf1-14e8-4d4e-a1fe-66b06c382eba">

<br><br>

## Monte-Carlo RL
- Markov Process와 달리 매 시행마다 나오는 결과의 기댓값을 더해서 value function을 계산한다 --> 계산이 간략하고 직관적이다
- Monte-Carlo 추정법
```
# Monte-Carlo RL의 psuedo code
1. 상태s 에서의 기대 리턴을 평가하려면,
2. 한 에피소드에서 상태 s에 처음 방문한 시간 : t
3. 카운터 증가  : N(st) <-- N(st) + 1
4. 총 리턴 증가 : S(s) <-- S(s) + Gt
5. 리턴의 평균을 추정 : V(s) = S(s) / N(s) 
```

<img width="600" src="https://github.com/namkidong98/SKT_FLY_AI_Challenger4/assets/113520117/3e6bffa6-1520-4877-8109-3c7119d82bbb">

