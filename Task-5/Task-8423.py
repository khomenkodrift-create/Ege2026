ans = []

for N in range(1 , 900_000):
    R = bin(N)[2:]
    if N % 5 == 0:
        R = R + bin(5)[2:]
    else:
        R = R + '1'
    if N % 7 == 0:
        R += bin(7)[2:]
    else:
        R += '1'
    R = int(R, 2)
    if R < 1_855_663:
        ans.append(N)
print(max(ans)) #463914