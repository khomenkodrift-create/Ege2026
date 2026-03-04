from itertools import product

alph = sorted('АВТОР')
word = 'ВАТА'
for pos, val in enumerate(product(alph, repeat=4), start=1):
    word_ = ''.join(val)
    if word_ == word:
        print(f'{pos}')
        break  # 146
