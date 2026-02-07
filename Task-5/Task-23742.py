ans = []

for N in range(1, 100_000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R = R + sum(map()