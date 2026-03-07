from itertools import permutations

cnt = 0
for val in set(permutations('ПАРИЖАНКА')):
    val = ''.join(val)
    if val.count('АА') + val.count('ИА') + val.count('АИ') == 1 and 'ААА' not in val:
        cnt += 1
print(cnt)