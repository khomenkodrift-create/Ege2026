def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for N in range(3, 100_000):
    R = convert(N, 3)
    if N % 3 == 0:
        R = R + R[-2:]
    else:
        ost = 3 * (N % 3)
        ost_3 = convert(ost, 3)
        R = R + ost_3
    R = int(R, 3)
    if R <= 150:
        ans.append(N)
print(max(ans))