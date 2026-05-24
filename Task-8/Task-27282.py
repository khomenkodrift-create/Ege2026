from itertools import product, repeat
from string import printable


cnt = 0
for val in product(printable[:13], repeat=6):
    val = ''.join(val)
    if val.count('0') == 0:
        cnt += 1
    s = printable[9:13]
    n = s.replace(s, '*')
    if '**' in val:
        cnt += 1

print(cnt)
#2985984 (странно)