num = 14**1402 + 28**501 - 14**51 - 1400

from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]
print(convert(num, 14).count('c')) #8