from itertools import product, repeat

alph = sorted('СТРОКА')
ans = []
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 != 0 and val[0] not in 'АЛ' and val.count('С') == 1:
        ans.append(pos)
print(max(ans))