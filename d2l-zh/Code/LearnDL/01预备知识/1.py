import torch

print(torch.cuda.is_available())
x = torch.arange(12)
print(x + 1)
print(x)
