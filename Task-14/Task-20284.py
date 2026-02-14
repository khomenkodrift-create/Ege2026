def convert_2(num, sys):
    res = 0
    for i in range(len(num)):
        res += int(num[i], 36) * sys ** (len(num) - i - 1)
    return res

for x in range(42):
    num1 = convert_2(list('J569') + [str(x)], 42)
    num2 = convert_2(list('1') + [str(x)] + list('IA'), 42)
    num = num1 + num2
    if num % 155 == 0:
        print(num // 155)

