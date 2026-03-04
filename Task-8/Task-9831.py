from string import printable
from itertools import product

cnt = 0
for val in product(printable[:16], repeat=3):
    val = ''.join(val)
    if val[0] != '0' and len(val) == len(set(val)):
        for i in printable[:16:2]:
            val = val.replace(i, '*')
        for i in printable[1:16:2]:
            val = val.replace(i, '_')
        if '**' not in val and '__' not in val:
            cnt += 1
print(cnt)