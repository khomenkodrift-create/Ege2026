from itertools import product
from string import printable

cnt = 0
for val in product(printable[:7], repeat=5):
    if val[0] != '0' and val.count('6') == 1:
