num = 6*144**26 + 11*12**75 - 48

from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]
print(convert(num, 12).count('b'))
