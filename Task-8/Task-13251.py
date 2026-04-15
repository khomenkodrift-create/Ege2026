from itertools import product, repeat

alph = 'КАЙФ'
cnt = 0
for val in product(alph, repeat=4):
    val = ''.join(val)
    if 'КФ' not in val and val[-1] != 'Й' and val.count('К') == 1 and val.count('А') == 1 and val.count('Й') == 1 and val.count('Ф') == 1:
        cnt += 1

print(cnt)