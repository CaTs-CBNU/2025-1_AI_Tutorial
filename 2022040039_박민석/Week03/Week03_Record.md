### Error Back Propagation Algorithm
##  Propagation : 번식
##  Gradient Descent(경사하강법)
    - 함수값이 낮아지는 방향으로 독립 변수 변경
    - 기울기를 기준으로 변경
    - 기울기 음수일 때 - 오른쪽, 기울기 양수일 떄 - 왼쪽 -> 0에 가까워질때까지 랜덤으로 박기
    - 1차적으로 근사값을 알아내기 위해 진행
    - 원래 모델에서는 그래프가 막 이게 막 이상할 수 있음. 그때 1차적으로 기울기가 0인 값을 찾는거임.
    - 하이퍼파라미터 : 우리가 정해줄 수 있는 파라미터
    - L : 손실함수, w : 가중치 -> 손실함수를 가중치로 미분한 기울기
    -> '학습률*기울기'를 가중치에서 빼줌
    - 에타가 너무 크면 step size가 너무 커서 손실이 클 수 있음. but 함수굴곡이 크면 step 사이즈가 클 수록 빠르게 global minimum을 찾을 수 있음.
    - step이 너무 작으면 local minimum에서 머물기만 할 수 있음. 자원, 시간적으로 낭비 큼.
    - 적절한 step size를 정해줘야함. -> 노가다
    - local minimum에 갖혀있을 수 있다는 것이 경사하강법의 한계

##  Error Back ~
#   가중치 업데이트를 통한 최적화
    - 알아서 가중치를 찾아주는 것이 딥러닝의 Error Back Propagation 이다.
    - 레이어가 크기때문에 파라미터를 자동으로 설정해줘야 함.
#   1. Feed Forward(순전파)
    - 신경망을 설정, 입력만 넣고 출력만 받는 것
    - Error을 기반으로 학습
    -> Error는 기존의 값에서 구한 값의 절대값을 뺀 값
    - net : 전에있던 입력값들을 더해주는 층
    - out : net값에 손실함수를 가해줘서 만든 층
    - 이번에 사용하는 손실 함수 : 시그모이드 함수
    - Error (MSE) : ((target - output)**2)/(결과값의 개수) 의 합
#   2. Back Propagation
    - 에러를 구한 것을 기반으로 출력층에서 입력층의 방향으로 가중치를 변경하는 것
    - 전체손실함수/가중치 = 전체손실함수/output * output/net * net/w -> 체인 룰
    - 경사하강법을 이용해서 가중치 변경
    - 이전 노드에서의 Back Propagation : 출력층
    - 출력층과 이전층은 그 전꺼의 에러만 반영해주면 됨.(case1) 출력층의 이전층과 그 이전층은 그 사이에 있는 노드의 에러를 반영해줘야함.(case2)
    - Error 값은 뒤로 갈수록 점점 커짐.

loader : 데이터셋 로드
shuffle : 무작위 셔플
generator : 시드 고정 - 비교를 위해서

torch.nn : torch 에서 제공하는 딥러닝 관련 lib
활성화 함수 = 손실 함수

CrossEntropyLoss : 손실함수 - 손실함수의 가중치가 0이 나오지 않게
optimizer : 경사하강법
SGD : 확률적 경사 하강법
step 지정 : learning rate

model(x) -> 모델에 x값을 넣으면 순전파
loss -> target-output
zero_grad -> 가중치를 0으로 초기화(처음 했던 학습이 다음의 학습에 영향을 주기 때문에 없애줘야함.)
backward -> 역전파
optimizer.step -> 가중치 업데이트

with torch.no_grad -> 모델의 값을 넣는 것이 즉, 테스트 데이터 넣는 것이 모델 학습에 영향을 주지 않도록 하는 것
dim=1 -> 출력값의 차원에서 최댓값
predicted == y : 예측한 것이 y의 값이 맞는지

