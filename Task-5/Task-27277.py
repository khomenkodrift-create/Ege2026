def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 10_000):
    n = convert(N, 3)
    if N % 3 != 0:
        n = '1' + n + n[-3:]
    else:
        n += convert(sum(int(i) for i in n) * 8, 3)
    R = int(n, 3)
    ans.append([abs(1220 - R), R])

print(min(ans))