from math import ceil, log2

L = 250
N = 1650 + 10
i = ceil(log2(N))
I = ceil(L * i / 8)
print(I * 65536 / 1024) #тк Кбайты