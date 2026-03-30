from math import ceil, log2

for N in range(1, 10**6):
    L = 105
    i = ceil(log2(N))
    I = ceil(L * i/ 8)
    if I * 65536 >= 7 *1024*1024:
        print(N)
        break
