from itertools import product, repeat

alph = sorted('АРГУМЕНТ')
ans = []
for pos, val in enumerate(product(alph, repeat=4), start=1):
    val = ''.join(val)
    if len(set(val)) == 4 and list(val) == sorted(val):
        ans.append(pos)
print(max(ans))