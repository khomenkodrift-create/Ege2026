from math import log2, ceil
for N in range(1, 10**6):
    L = 377
    i = ceil(log2(N))
    I = ceil(L * i/ 8)
    if I * 23155 > 5536*1024:
        print(N)
        break #33