from math import ceil, log2
for N in range(1 , 100_000):
    i = ceil(log2(N))
    L = 119
    I = ceil(L * i / 8)
    if 125300 * I > 23 * 1024 * 1024:
        print(N)
        break

