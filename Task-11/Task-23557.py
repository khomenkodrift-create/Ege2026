from math import log2, ceil
for L in range(1, 10**6):
    N = 10 + 52 + 500
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 45877 * I > 49 * 1024 * 1024:
        print(L)
        break # 896
