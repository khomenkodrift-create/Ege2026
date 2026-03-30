from itertools import product
ans = []
alph = sorted('ГРАНИТ')

for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[0] not in 'АИГ' and val.count('А') == 1 and pos % 2 == 1:
        ans.append(pos)
print(ans)
#23589