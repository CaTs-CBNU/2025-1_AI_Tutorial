#인공지능_2주차

##뉴럴 네트워크
 - 인공지능 : 인간의 뉴런을 본 따 어떠한 기능을 만드는 것
 - 시냅스 조절 : 가중치 조절(in 인공지능)
 - Scaling Factor : 각 정보의 가중치에 따라 입력한 정보를 얼마나 넣을지 정하는 것
 - First Funtion에서 net 값을 통해 한계점 도달하면 Second Function에서 이전까지 0이다가 1값 도출

##연결강도
 - Perceptron = Cell body -> 한계치가 되면 출력 (활성화 함수)
 - Connection weight = 뉴런의 연결 강도(양이온의 이동 정도) 
 - Scaling Factor = Connection weight -> 정보의 크기를 조정하기 때문
 -  입력 정보 x를 w에 따라서 가중치를 정함. 

##Perceptron
 - Second Function : Hard Limit Function
 - 입력받은 정보 x와 w를 다 더한 값이 Hard Limit Function에 의해서 0으로 나오면 y = 0, 1로 나오면 y=1
   (즉, Hard Limit Function은 정보의 크기에 따라 출력을 조절함. -> 입력이 음수 : 0, 입력이 양수 : 1)
 - 편형(bias값): Layer Perceptron에서 원하는 값을 정해주기 위해 임의적으로 정해줌. x=1

##Single Layer Perceptron
 - 초록 값 : AND연산값, OR연산값, NAND연산값에 따른 y=1이 되는 값
 - not operation : perceptron을 이용해서 선형 구분이 가능해지게 함.

##Multi Layer Perceptron
 - XOR
 - 선형적으로 주어진 Perceptron을 모아서 값을 만들면 비선형적인 연산값을 구할 수 있다.