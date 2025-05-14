import torch
import torch.nn as nn

#활성화 함수
def step(x):
    return torch.where(x >=0, 1, 0)

class Perceptron(nn.Module):
    def __init__(self, weights, bias):
        super().__init__()
        self.weights = torch.tensor(weights, dtype = torch.float)
        self.bias = torch.tensor(bias, dtype = torch.float)
    
    def forward(self, x):
        z = torch.matmul(x, self.weights) + self.bias
        return step(z)

inputs = torch.tensor([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]
])


print("AND 퍼셉트론 결과")
and_perceptron = Perceptron(weights = [1.0, 1.0], bias=-1.5)

for x in inputs:
    x=x.float()
    out = and_perceptron(x.float())
    print(f"입력: {x.tolist()} --> 출력: {int(out.item())}")
print()


print("OR 퍼셉트론 결과")
or_perceptron = Perceptron(weights=[1.0, 1.0], bias=-0.5)
for x in inputs:
    out = or_perceptron(x)
    print(f"입력: {x.tolist()} --> 출력: {int(out.item())}")
print()


print("NAND 퍼셉트론 결과")
nand_perceptron = Perceptron(weights=[-1.0, -1.0], bias=1.5)
for x in inputs:
    out = nand_perceptron(x)
    print(f"입력: {x.tolist()} --> 출력: {int(out.item())}")
print()


print("XOR 퍼셉트론 결과")
for x in inputs:
    x = x.float()

    # 은닉층: NAND, OR
    nand_out = nand_perceptron(x)
    or_out = or_perceptron(x)

    # 출력층: AND
    hidden = torch.tensor([float(nand_out.item()), float(or_out.item())])
    xor_out = and_perceptron(hidden)

    print(f"입력: {x.tolist()} --> 출력: {int(xor_out.item())}")