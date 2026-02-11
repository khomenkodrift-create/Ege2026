def convert(num, sys):
    res = ''
    while num:
        num += str(num, sys)
        num //= sys
    return res[::-1]

ans = []


for N in range(1, 100_000):
    R = convert(N, 3)
    if N % 3 == 0:
