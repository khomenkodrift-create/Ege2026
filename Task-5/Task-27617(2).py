ans = []
for N in range(1, 100_000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R = R + R[-3:]
    else:
        ost = (N % 3) * 3
        ost_2 = bin(ost)[2:]
        R = R + ost_2
    R = int(R, 2)
    if 110 < R < 150:
        print(R, N)
        #31