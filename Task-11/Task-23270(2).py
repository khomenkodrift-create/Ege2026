from math import ceil, log2

for L in range(1, 10**6):
    N = 27 + 10
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 3548 > 12 * 1024:
        print(L)
        break