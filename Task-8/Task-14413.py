from itertools import permutations
cnt = 0
for val in set(permutations('СОРТИРОВКА')):
    val = ''.join(val)
    if len(val):
        for i in permutations('СРТРВК'):
            val = val.replace(i, '*')
        for i in permutations('ОИОА'):
            val = val.replace(i, '-')
        if '***' not in val and '---' not in val:
            cnt += 1
print(cnt)