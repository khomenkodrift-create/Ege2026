def convert(num, sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]

for x in range(1, 10001):
    num = convert(3**2000 + 3**10 - x, 3)
    if num.count('2') == 2000:
        print(x)
        break