def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for x in range(0, 1000):
    num = 3*7**(x+1) + 13*7**(x + 2) + 31*7**(3*x) + 1*7**(2*x)
    num_7 = convert(num, 7)
    summ = sum(map(int, num_7))
    if summ == 18:
        print(x)
        break # прерывает (тк первый попавший подойдет)