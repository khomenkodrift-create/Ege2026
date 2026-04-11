ans = []
for N in range(1, 100000):
    R = bin(N)[2:]
    R_ost = sum(map(int, R)) % 2
    R_2 = R + str(R_ost)
    R_2_ost = sum(map(int, R_2)) % 2
    R_fin = R_2 + str(R_2_ost)
    Res = int(R_fin, 2)
    if Res > 253:
        ans.append(N)

print(min(ans))
#64
