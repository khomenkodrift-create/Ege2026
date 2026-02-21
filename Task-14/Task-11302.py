from string import printable
for x in printable[:25]:
    num1 = int(f'488926{x}9', 25)
    num2 = int(f'8378{x}2678', 25)
    num3 = int(f'624{x}7', 25)
    num4 = int(f'4{x}691', 25)
    num5 = int(f'737{x}9{x}89', 25)
    num = num1 + num2 + num3 + num4 + num5
    if num % 24 == 0:
        print(num // 24)
