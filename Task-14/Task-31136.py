from string import printable

for x in printable[:23]:
    num1 = int(f'81{x}9982', 23)
    num2 = int(f'36{x}24', 23)
    num3 = int(f'72{x}5', 23)
    num = num1 + num2 + num3
    if num % 22 == 0:
        print(num // 22)