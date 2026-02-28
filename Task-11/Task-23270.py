from math import ceil, log2
for L in range(1, 10**6):
    N = 10 + 27
    i = ceil(log2(N))
    I = ceil(L* i/8)
    if 3548 * I > 12 * 1024:
        print(L)
        break #5