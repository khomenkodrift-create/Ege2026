ans = []

def convert(num, sys):
    res = ''
    while num:
        res += str(num, sys)
        num //= sys
    return res[::-1]

for N in range(1, 100_000):
    if