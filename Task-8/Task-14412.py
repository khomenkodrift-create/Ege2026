from itertools import product
alph = 'АЛГОРИТМ'
for pos, val in enumerate(product(alph, repeat=6)):
    val = ''.join(val)
    if 0 < val.count()