from itertools import product
alph = sorted('МИЗАНТРОП')
ans = []
for pos, val in enumerate(product(alph, repeat=5), start =1):
    if pos % 2 == 0 and val[0] == 'Н' and val.count('Р') == 2:
        ans.append(pos)

print(max(ans)) #32712