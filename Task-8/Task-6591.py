from itertools import product
from string import printable

cnt = 0
for val in product(printable[:7], repeat=5):
    if val[0] != '0' and val.count('6') == 1:
        num = [int(d) for d in val] #Создаём список чисел, переводя каждый символ d из val в целое число.
        sum_chetnie = sum(x for x in num if x % 2 == 0)                   #Например, если val = ('1', '2', '3', '4', '5'),
        sum_nechetnie = sum(x for x in num if x % 2 == 1)                 #то num = [1, 2, 3, 4, 5].
        if sum_chetnie < sum_nechetnie:
            cnt += 1
print(cnt)