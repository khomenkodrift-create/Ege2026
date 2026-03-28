from string import printable
from itertools import product
ans = []
for pos, val in enumerate(product(printable[:9], repeat=6), start=1):
    left = val[:3]
    right = val[3:]
    sum_left = sum(int(val) for val in left)
    sum_right = sum(int(val) for val in right)
    s_left = str(left)
    s_right = str(right)
    all_digits = set(s_left + s_right)
    if sum_left == sum_right and len(all_digits) == len(s_left + s_right):
        ans.append(pos)
print(ans)