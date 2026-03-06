from string import printable
from itertools import product
cnt = 0
for val in product(printable[:16], repeat=4):
    val = ''.join(val)
    if val[0] != '0' and val.count('3') == 1 and all(val[i] != val[i + 1] for i in range(len(val) - 1)):
            cnt += 1
print(cnt)