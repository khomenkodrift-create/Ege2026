ans = []

for N in range(1, 100_000):
    R = bin(N)[2:]
    if N % 5 == 0:
        R = R + '11'
    else:
        R = R + bin(N // 5)[2:]
    R = int(R, 2)
    if R > 896:
        ans.append(N)
print(min(ans)) # 56