from math import ceil, log2
for N in range(1, 10 ** 10):
    L = 1231
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 523872 > 432 * 1024 * 1024:
        print(N)
        break
        #33