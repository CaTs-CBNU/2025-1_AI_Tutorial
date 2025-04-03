import torch
import torch.nn as nn

def step(x):
    return torch.where(x>=0,1,0)

class Perceptron(nn.Module):
    def __init__(self, weights, bias):
        super().__init__()
        self.weights = torch.tensor(weights, dtype=torch.float)
        self.bias = torch.tensor(bias, dtype=torch.float)

    def forward(self, x):
        z = torch.matmul(x, self.weights) + self.bias
        return step(z)
    

# 입력 정의
inputs = torch.tensor([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]   
])


# AND 퍼셉트론 만들기
print("AND 퍼셉트론 결과")
and_perceptron = Perceptron(weights=[1.0, 1.0], bias=-1.5)

for x in inputs:
    x=x.float()
    out = and_perceptron(x.float())
    print(f"입력 : {x.tolist()} -> 출력 : {int(out.item())}")
print()

# OR 퍼셉트론 만들기
print("OR 퍼셉트론 결과")
or_perceptron = Perceptron(weights=[1.0, 1.0], bias=-0.5)

for x in inputs:
    x=x.float()
    out = or_perceptron(x.float())
    print(f"입력 : {x.tolist()} -> 출력 : {int(out.item())}")
print()

# NAND 퍼셉트론 만들기
print("NAND 퍼셉트론 결과")
nand_perceptron = Perceptron(weights=[-1.0, -1.0], bias=1.5)

for x in inputs:
    x=x.float()
    out = nand_perceptron(x.float())
    print(f"입력 : {x.tolist()} -> 출력 : {int(out.item())}")
print()

# XOR 퍼셉트론 만들기
print("XOR 퍼셉트론 결과")

for x in inputs:
    x=x.float()
    na_out = nand_perceptron(x.float())
    o_out = or_perceptron(x.float())
    out = na_out*o_out
        
    print(f"입력 : {x.tolist()} -> 출력 : {int(out.item())}")
print()
