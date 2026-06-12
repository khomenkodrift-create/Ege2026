from itertools import product, repeat

alph = sorted('ЦИТРУС')

ans = []

for pos, val in enumerate(product(alph, repeat= 5), start=1):
    val = ''.join(val)
    if val.count('И') == 2 and 'ЦЦ' not in val:
        ans.append(pos)
print(max(ans))
