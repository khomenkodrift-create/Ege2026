from itertools import product
alph = 'КОТБУС'
cnt = 0
for val in product(alph, repeat=8):
    val = ''.join(val)
    if val[0] not in 'ОУ' and 'КОТ' in val:
        cnt += 1
print(cnt)