from itertools import product, repeat
from string import printable

cnt = 0

for val in product(printable[:9], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('3') == 2:
        for i in printable[1:9:2]:
            val = val.replace(i, '*')
        if '*2' not in val and '2*' not in val:
            cnt += 1

print(cnt)

#или
from itertools import product

alph = sorted('АКЦЕНТ')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[0] not in 'АЕК' and val.count('Т') >= 1:
        print(pos)
        break

from itertools import product

alph = sorted('АКЦЕНТ')
ans = []
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[0] not in 'АЕК' and val.count('Т') >= 1:
        ans.append(pos)
print(min(ans))

from itertools import product

alph = sorted('ГРАФИН')
ans = []
for pos, val in enumerate(product(alph, repeat=5), start= 1):
    val = ''.join(val)
    if pos % 2 != 0 and val[0] in 'ГРФ' and val.count('А') >= 1:
        ans.append(pos)
print(max(ans))


