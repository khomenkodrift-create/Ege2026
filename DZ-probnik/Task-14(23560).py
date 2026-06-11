from string import printable
from string.templatelib import convert


def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]
ans = []
for x in range(1, 2400):
    num = convert(7 * 9 ** 210 + 6 * 9 ** 110 - x, 9)
    if num.count('0') == 100:
        ans.append(x)
print(max(ans))
