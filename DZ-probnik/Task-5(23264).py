def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'
ans = []
for N in range(1, 100_000):
    R = convert(N, 3)
    if N % 3 == 0:
        R = R + R[-2:]
    else:
        ost = (N % 3) * 5
        ost_3 = convert(ost, 3)
        R = R + ost_3
    R = int(R, 3)
    if R > 150:
        ans.append(R)
print(min(ans))