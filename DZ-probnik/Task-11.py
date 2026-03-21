from math import ceil, log2
for L in range(1, 10**6):
    N = 25 + 487
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 345 * I > 70 * 1024:
        print(L)
        break
