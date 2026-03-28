from itertools import product, repeat
ans = []
alph = sorted('МЫСЛЬ')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[0] == 'Ы' and val[1] == 'Ы':
        ans.append(pos)
print(ans)
#2374