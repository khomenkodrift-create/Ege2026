from itertools import product, repeat

alph = sorted('АПРЕЛЬ')
ans = []
for pos, val in enumerate(product(alph, repeat=5), start=1):
    if pos % 2 == 0 and val[0] != 'Ь' and val[0] != 'Р' and val.count('Л') >= 2:
        ans.append(pos)
print(max(ans))
