def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


num = 7*729**543 - 6*81 - 5*9**987 - 20
print(convert(num, 9).count('8'))

# или

num = 7*729**543 - 6*81 - 5*9**987 - 20

cnt = 0
while num:
    if num % 9 == 8:
       cnt += 1
    num //= 9
print(cnt)