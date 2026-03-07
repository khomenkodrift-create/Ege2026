from string import printable
from itertools import product

cnt = 0
for val in product(printable[:8], repeat=10):
    val = ''.join(val)
    if val[0] != '0' and val.count('7') == 5:
        if all(not (val[i] == '7' and ((i > 0 and val[i - 1].isdigit() and int(val[i - 1]) % 2 == 1) or (i < len(val) - 1 and val[i + 1].isdigit() and int(val[i + 1]) % 2 == 1))) for i in range(len(val))):
            cnt += 1
print(cnt)
