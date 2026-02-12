def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

num = 51*7**12 - 7**3 - 22
print(sum(map(int, convert(num, 7)))) # 70