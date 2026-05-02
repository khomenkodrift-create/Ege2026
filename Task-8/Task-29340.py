from itertools import product, repeat

alph = sorted('АПРЕЛЬ')
ans = []
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[0] != 'А' and val[0] != 'Л' and val.count('П') >= 2 and pos % 2 != 0:
        ans.append(pos)

print(min(ans))
#7903