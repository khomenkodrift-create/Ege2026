def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num // sys
    return res[::-1]
for N in range(1, 100_000):
    R = convert(N, 3)
    if R % 3 != 0:
        R = '1' + R + R[-3:]
    else:
        r = sum(map(R)) * 8
        R = R + convert(r, 3)