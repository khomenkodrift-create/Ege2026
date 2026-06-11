from math import ceil, log2
for L in range(1, 10 ** 10):
    N = 52 + 52 + 963 + 10
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 2000 <= 693 * 1024:
        print(L)
        #257
