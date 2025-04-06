import torch
import torch.nn as nn

#활성화 함수(양수면 1 아니면 0)
def step(x):
  return torch.where(x>=0,1,0)

class Perceptron(nn.Module):
  def __init__(self, weights, bias):
    super().__init__()
    self.weights=torch.tensor(weights, dtype=torch.float)
    self.bias=torch.tensor(bias, dtype=torch.float)

  def forward(self,x):
      z=torch.matmul(x,self.weights)+self.bias
      return step(z)

# 입력 값들
inputs = torch.tensor([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]
])

# AND 퍼셉트론
print("퍼셉트론 결과 - AND")
and_perceptron = Perceptron([1.0, 1.0], -1.5)
for x in inputs:
    print(f"{x.tolist()} -> {int(and_perceptron(x).item())}")
print()

# OR 퍼셉트론
print("퍼셉트론 결과 - OR")
or_perceptron = Perceptron([1.0, 1.0], -0.5)
for x in inputs:
    print(f"{x.tolist()} -> {int(or_perceptron(x).item())}")
print()

# NAND 퍼셉트론
print("퍼셉트론 결과 - NAND")
nand_perceptron = Perceptron([-1.0, -1.0], 1.5)
for x in inputs:
    print(f"{x.tolist()} -> {int(nand_perceptron(x).item())}")
print()

# XOR 퍼셉트론 
print("퍼셉트론 결과 - XOR")
for x in inputs:
    nand_out = nand_perceptron(x)
    or_out = or_perceptron(x)
    combined = torch.tensor([nand_out.item(), or_out.item()], dtype=torch.float)
    xor_out = and_perceptron(combined)
    print(f"{x.tolist()} -> {int(xor_out.item())}")
