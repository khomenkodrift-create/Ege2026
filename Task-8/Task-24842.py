from itertools import permutations, product
cnt = 0
alph = 'ЕГЭ2026'
for val in product(alph, repeat=6):
    val = ''.join(val)
    if val.count('2') == 4 and val.count('6') == 0:
        cnt += 1
    if val.count('2') == 1 and val.count('6') == 1:
        cnt += 1
print(cnt)

#ПРОВЕРИТЬ + ЗАПУШИТЬ(NO INTERNET COS OF PIDORS)asdad