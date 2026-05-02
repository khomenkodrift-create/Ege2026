
for N in range(1, 100_000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R = R + R[-2:]
    else:
        R_ost = bin(3 *(N % 3))
        R = R + R_ost
    R = int(R, 2)
    if R in