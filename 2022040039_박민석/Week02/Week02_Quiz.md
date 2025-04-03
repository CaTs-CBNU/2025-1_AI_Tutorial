### Quiz 1
    Q1.Neural Network는 여러 개의 perceptron으로 구성된다.
    : o
    Q2.Neural Network의 connection weight의 값은 모두 달라야만 한다.
    : x (0만 아니면 상관 x)
    Q3.Connection weight은 해당 입력 값과 더해진다.
    : x (Connection weight은 해당 입력값과 곱해짐)
    Q4.Neural network는 일반적으로 layer 구조를 갖는다.
    : o
    Q5.아래 perceptron의 출력 값을 구하시오.(Activation function으로 hard limit 함수를 사용한다.)
    : 1*(-2) + 2*1 + 3*0.5 = 1.5
      1.5 > 0
      y=1
### Quiz 2
    Q1.Perceotron은 선형으로 분리 가능한 문제를 해결할 수 있다.
    : o
    Q2.AND 연산은 neural network으로 해결할 수 있다.
    : o
    Q3.XOR 연산은 perceptron으로 해결할 수 있다.
    : x
    Q4.Layer가 3개인 neural network은 임의의 함수를 모델링할 수 있다.
    : o
    Q5.주어진 perceptron이 아래의 이진논리 연산을 수행할 수 있는 w3의 범위를 결정하시오.
    (Activation Function으로는 아래 Hard Limit 함수를 사용한다.)
    : 2 (선형 구분으로 가능, x<=0 일때 y=0이므로 w3의 범위는 0<w3<1)