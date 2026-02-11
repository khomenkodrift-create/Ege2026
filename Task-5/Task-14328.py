ans = []
from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]
for N in range(1, 100_000):
    R = convert(N, 12)
    if N % 3 == 0:
        R = '1' + R + 'b'
    else:
        R = '2' + R + '0'
    R = int(R, 12)
    if R < 1996:
        ans.append(R)
print(max(ans)) # 1991