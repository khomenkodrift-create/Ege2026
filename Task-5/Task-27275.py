def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num // sys
    return res[::-1]
ans = []
for N in range(1, 100_000):
    R = convert(N, 3)
    if N % 3 == 0:
        R = '1' + R + '21'
    else:
        n = N % 3
        n_ = n * 5
        R = R + convert(n_, 3)
    R = int(R, 3)
    ans.append(N)
if ans % 2 == 1:
    print(max(ans))