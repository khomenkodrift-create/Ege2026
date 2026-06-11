from math import ceil, log2
for N in range(1 ,10**6):
    L = 25 + 10
    i = ceil(log2(N))
    I = ceil(L * i / 8) + 48


