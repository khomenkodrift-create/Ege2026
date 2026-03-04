from itertools import product

alph = sorted('ПАРУС')
word = 'УАПАП'
for pos, val in enumerate(product(alph, repeat=5), start=1):
    word_ = ''.join(val)
    if word_ == word:
        print(f'{pos}')
        break #2527