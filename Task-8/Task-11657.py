from itertools import permutations
cnt = 0
for val in permutations('0124567', r=6): #тк не содержит 3 - 0124567
    if val[0] != '0' :
        val = ''.join(val)
        i = val #тк В процессе замен строка i меняется, а исходная val остается для сравнения, если потребуется
        for m in '0246':
            i = i.replace(m, '*')
        if '**' in i:
            cnt += 1
print(cnt)
