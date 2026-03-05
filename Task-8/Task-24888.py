from string import printable
from itertools import product
cnt = 0
for val in product(printable[:16], repeat=4):
    val = ''.join(val)
    if val[0] != '0' and val.count('3') == 1 and len(val) == len(set(val)):
        for i in printable[:16]:
            val = val.replace(i, '*')
        if '**' not in val and '__' not in val:
            cnt += 1
print(cnt)