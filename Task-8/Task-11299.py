from itertools import product, repeat
ans = []
alph = sorted('БМЮРН')
for pos , val in enumerate(product(alph, repeat=6), start = 1):
    val = ''.join(val)
    if pos % 2 ==1 and val[0] != 'М' and val.count('Р') >= 2 and val.count('М') == 1:
        ans.append(pos)
print(max(ans))


