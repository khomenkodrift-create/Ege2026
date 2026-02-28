from itertools import product
alph = 'ЗЕРКАЛО'
cnt = 0
for val in product(alph, repeat=6):
    val = ''.join(val)
    if 0 < val.count('К') <= 4 and all(val.count(i) <= 1 for i in 'ЗЕРАЛО'):
        cnt += 1
print(cnt)