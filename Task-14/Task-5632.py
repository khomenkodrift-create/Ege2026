from string import printable
for x in printable[:21]:
    for y in printable[:21]:
        num1 = int(f'32{y}{x}A', 21)
        num2 = int(f'16{y}18', 21)
        num = num1 + num2
        if num % 12 == 0: #не закончено