from string import printable

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

for N in range(2, 37):
    if convert(41, N)[-1] == '2' and convert(131, N)[-1] == '1':
        print(N)
