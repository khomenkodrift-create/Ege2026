from itertools import product, repeat
from string import printable
cnt = 0
for val in product(printable[:7], repeat=7):
    val = ''.join(val)
    if val[0] not in '035':
        if not all(x in val for x in ['22', '44']):
# или   if ('22' not in val and '44' in val) or ('44' in val and '22' in val) or ('22' and '44' not in val)
            cnt += 1
print(cnt)