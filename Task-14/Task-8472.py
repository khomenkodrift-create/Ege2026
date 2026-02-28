def convert(num, sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]
for x in range(100):
    num_1 = 7*100**6 + int('A', 36)*100**5 + x*100**4 + 0*100**3 + 1*100**2 + 2*100**1 + 3*100**0
    num_2 = 1*100**5 + int('B', 36)*100**4 + int('A', 36)*100**3 + 6*100**2 + 4*100**1 + x*100**0
    num_3 = x*100**6 + 9*100**5 + 8*100**4 + 0*100**3 + 1*100**2 + 2*100**1 + int('C', 36)*100**0
    num = num_1 - num_2 + num_3
    if num % 21 == 0:
        print(convert(num // 21, 6)) #13350155514402111