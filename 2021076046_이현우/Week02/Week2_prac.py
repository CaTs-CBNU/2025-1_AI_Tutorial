import torch
import torch.nn as nn

def step(x): #활성화 함수
    return torch.where(x >= 0, 1, 0) 
# where() 함수를 통해 입력값 x에 조건식을 만족하면(0이상이라면) 0또는 1을 담은 텐서를 반환

class Perceptron(nn.Module): ## 객체를 호출하면 내부적으로 forward() 함수를 실행할 것.. 
    def __init__(self, weights, bias): # 가중치와 편향값을 입력받아 
        super().__init__()
        self.weights = torch.tensor(weights, dtype=torch.float) #파이토치 텐서로 변환!
        self.bias = torch.tensor(bias, dtype=torch.float) 

    def forward(self, x): 
        z = torch.matmul(x, self.weights) + self.bias # 입력 x와 가중치의 내적과 편향을 더함
        return step(z)

inputs = torch.tensor([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]
])

#퍼셉트론을 통한 논리게이트 생성 테스트

print("AND 퍼셉트론 결과")
and_perceptron = Perceptron(weights = [1.0, 1.0], bias=-1.5) 

for x in inputs:
    x = x.float() # 계산 중 자료형 불일치를 방지
    out = and_perceptron(x.float())
    print(f"입력: {x.tolist()} -> 출력: {int(out.item())}") 
    # .list()를 통해 텐서를 파이썬 리스트로 변환
    # .item()을 통해 값이 하나인 텐서에서 값 가져오기
print()

print("OR 퍼셉트론 결과")
or_perceptron = Perceptron(weights = [1.0, 1.0], bias=-0.5)

for x in inputs:
    x = x.float()
    out = or_perceptron(x.float())
    print(f"입력: {x.tolist()} -> 출력: {int(out.item())}")
print()

print("NAND 퍼셉트론 결과")
nand_perceptron = Perceptron(weights = [-1.0, -1.0], bias=1.5)

for x in inputs:
    x = x.float()
    out = nand_perceptron(x.float())
    print(f"입력: {x.tolist()} -> 출력: {int(out.item())}")
print()


print("XOR 퍼셉트론 결과")
xor_second_perceptron = Perceptron(weights = [1.0, -1.0], bias=-0.5)

for x in inputs:
    x = x.float() 
    or_out = or_perceptron(x) # OR 퍼셉트론의 결과 저장
    and_out = and_perceptron(x) # AND 퍼셉트론의 결과 저장
    xor_input = torch.stack([or_out, and_out]) # stack() 함수를 사용하여 텐서를 모아서
    out = xor_second_perceptron(xor_input.float()) # 다음 레이어에게 전달!
    print(f"입력: {x.tolist()} -> 출력: {int(out.item())}")
print()