def convert(N):
    res = ''
    while N > 0:
        res = str(N % 3) + res
        N //= 3
    return res

cnt = 0
for N in range(10, 10000):
    s = convert(N)
    if N % 5 == 0:
        s = s[-2:] + s
    else:
        rem = (N % 5) * 4
        s = s + bin(rem)[2:]
    if len(s) % 2 == 0:
        s += '0'
    else:
        s += '1'

    R = int(s, 3)
    if R < 23945:
        cnt += 1
print(cnt)

