from string import printable
from itertools import product

cnt = 0
for val in product(printable[:20], repeat=10):
    val = ''.join(val)
    if val[0] != 0 and val[-1] + val[-2] == 26:
        for i in printable[:20:2]:
            val = val.replace(i, '*')
        for i in printable[1:20:2]:
            val = val.replace(i, '-')
        if '--' not in val and '**' not in val:
            cnt += 1
print(cnt)
