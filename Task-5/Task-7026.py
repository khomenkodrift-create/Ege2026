ans = []

for N in range(9, 100_000): # при N больше 8 берем на 1 больше
    R = bin(N)[2:]
    if N % 2 == 0:
        R = '1' + R + '00'
    else:
        R = R + bin(sum(map(int, R)))[2:]

    R = int(R, 2)
    if R > 88:
        ans.append([R, N])
print(min(ans)) #25
