from itertools import product, repeat

alph = sorted('ШКОЛА')
ans = []
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val == 'ШАЛАШ':
        ans.append(pos)
print(ans)
#2555
