from itertools import product
alph = sorted('ЯНВАРЬ')
for pos, val in enumerate(product(alph, repeat=5), start = 1):
    word = ''.join(val)




