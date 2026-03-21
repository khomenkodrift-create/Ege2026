from string import printable
from itertools import product, repeat

cnt = 0
for val in product(printable[:9], repeat=7):
    val = ''.join(val)
    if val[0] != '0' and val[0] in '2468' and val[-1] in '124578' and val.count('6') >= 1:
        cnt += 1
print(cnt) #827352 (потом и мучениями)