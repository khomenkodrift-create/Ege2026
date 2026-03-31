from itertools import product, repeat
from string import printable
cnt = 0
for val in product(printable[:7], repeat=7):
    val = ''.join(val)
    if val[0] != '0' and val[0] != '3' and val[0] != '5':
        val = val.replace('22', '*')
        val = val.replace('44', '-')
        if '*' not in val and '-' not in val:
            cnt += 1
print(cnt)
#470596