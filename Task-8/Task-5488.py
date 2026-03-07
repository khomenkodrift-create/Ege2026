from itertools import product
alph = 'ПОЛИНА'
glasnie = 'ОИА'
soglasnie = 'ПЛН'
cnt = 0
for val in (product(alph, repeat=8)):
    val = ''.join(val)
    if sum(val.count(i) for i in 'ОИА') < sum(val.count(i) for i in 'ПЛН'):
        cnt += 1
print(cnt) #610173
