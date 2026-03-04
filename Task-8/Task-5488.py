from itertools import product
alph = 'ПОЛИНА'
glasnie = 'ОИА'
soglasnie = 'ПЛН'
cnt = 0
for pos, val in enumerate(product(alph, repeat=8)):
    val = ''.join(val)
    glasnie_count = sum(1 for i in val if i in glasnie)
    soglasnie_count = sum(1 for i in val if i in soglasnie)
    if soglasnie_count > glasnie_count:
        cnt += 1
print(cnt) #610173

# я написал в if all(val.count(i) for i in 'ОИА') < all(val.count(n) for n in 'ПЛН')