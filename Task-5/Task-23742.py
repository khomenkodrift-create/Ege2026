ans = []

for N in range(1, 100_000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R += R[-3:]
    else:
        R += bin(N % 3 * 3)[2:]
    R = int(R, 3)
    if R > 200:
        ans.append(R)

print(min(ans)) # 274