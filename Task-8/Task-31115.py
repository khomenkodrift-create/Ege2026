from itertools import product
alph = sorted('АКЦЕНТ')
ans = []
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 == 0 and val[0] not in 'АЕК' and val.count('Ц') >= 2:
        ans.append(pos)
print(min(ans))