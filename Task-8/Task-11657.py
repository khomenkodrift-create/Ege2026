from itertools import product, repeat
from string import printable
cnt = 0
for val in product(printable[:8], repeat=6):
    val = ''.join(val)
    if val[0] != 0 and '3' not in val and len(val) == len(set(val)):
        for i in printable[:8:2]:
            val = val.replace(i, '*')
        if '**' in val:
            cnt += 1

print(cnt)
