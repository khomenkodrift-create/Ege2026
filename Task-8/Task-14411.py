from itertools import product, repeat

alph = sorted('АБИЛМСУЦ')
cnt
for pos, val in enumerate(product(alph, repeat=5)):
    val = ''.join(val)
    if val[-1] != 'Я' and
