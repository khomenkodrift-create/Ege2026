from math import remainder

ans = []


def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


for N in range(1, 900_000):
    R = convert(N, 3)
    s = sum(map(int, R))
    if s % 9 == 0:
        R = R + '2'
    else:
        r = s % 9
        res = ''
        while r > 0:
            res = str(r % 3) + res
            r //= 3
        R = R + res
    R = int(R, 3)
    if N > 166:
        ans.append(R)
print(min(ans)) # 647 (почти ниче не понял)
