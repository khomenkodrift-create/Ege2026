from math import ceil, log2
for L in range(1, 100000):
    N = 10 + 17
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 7_564_230 > 31 * 1024 * 1024:
        print(L)
        break
        #7