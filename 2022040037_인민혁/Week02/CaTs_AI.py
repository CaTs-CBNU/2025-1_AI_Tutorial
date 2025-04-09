import torch
import torch.nn as nn

def step(x):
    return torch.where(x>=0, 1, 0)

class Perceptron(nn.Module):
    def __init__(self, weight, bias):
        super().__init__()
        self.weight = torch.tensor(weight, dtype=torch.float)
        self.bias = torch.tensor(bias, dtype=torch.float)
    def forward(self, x):
        z = torch.matmul(x, self.weight) + self.bias
        return step(z)
    
inputs = torch.tensor([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]
])

print("AND Perceptron Result")
and_perceptron = Perceptron(weight=[1.0,1.0], bias=-1.5)

for x in inputs:
    x = x.float()
    out = and_perceptron(x.float())
    print(f"입력: {x.tolist()} -> 출력: {int(out.item())}")
print()

print("OR Perceptron Result")
or_perceptron = Perceptron(weight=[1.0,1.0], bias=-0.5)

for x in inputs:
    x = x.float()
    out = or_perceptron(x.float())
    print(f"입력: {x.tolist()} -> 출력: {int(out.item())}")
print()

print("NAND Perceptron Result")
nand_perceptron = Perceptron(weight=[-1.0,-1.0], bias=1.5)

for x in inputs:
    x = x.float()
    out = nand_perceptron(x.float())
    print(f"입력: {x.tolist()} -> 출력: {int(out.item())}")
print()