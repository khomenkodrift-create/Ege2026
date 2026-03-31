def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for N in range(1, 100_000):
    R = convert(N, 4)
    if N % 4 == 0:
        R = R[:3] + R
    else:
        ost= N % 4
        ost_4 = convert(ost * 4, 4)
        R = R + ost_4
    R = int(R, 4)
    if R > 291:
        ans.append(R)
print(min(ans))
#296