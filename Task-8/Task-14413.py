from itertools import permutations
cnt = 0
for val in set(permutations('СОРТИРОВКА')): # для одинаковых букв
    val = ''.join(val)
    for i in 'СРТРВК':
        val = val.replace(i, '*')
    for i in 'ОИОА':
        val = val.replace(i, '-')
    if '***' not in val and '---' not in val:
        cnt += 1
print(cnt)