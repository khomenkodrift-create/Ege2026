from itertools import product
def proverka(val):
    for i in range(len(val) - 1):
        if val[i] > val[i + 1]: return False
    return True
ans = []
alph = sorted('АРГУМЕНТ')
for pos, val in enumerate(product(alph, repeat=4), start=1):
    val = ''.join(val)
    if len(val) == len(set(val)) and (proverka(val)==True):
        ans.append(pos)
print(max(ans))