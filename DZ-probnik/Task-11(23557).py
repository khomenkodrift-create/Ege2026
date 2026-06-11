from math import ceil, log2

for L in range(1, 10 ** 10):
    N = 10 + 52 + 52 + 500
    i = ceil(log2(N))
    I = ceil(L *  i/ 8)
    if I * 45877 > 49 * 1024 * 1024:
        print(L)
        break