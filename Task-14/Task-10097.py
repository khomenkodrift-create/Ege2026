from string import printable

def convert(num, sys):
    res = ''
    while num:
        res += printable[num%sys]
        num //= sys
    return res[::-1]
num = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024
print(num.count('0'))