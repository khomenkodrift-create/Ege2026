from string import printable
for x in printable[:15]:
    num1 = int(f'432{x}3', 15)
    num2 = int(f'86{x}86', 15)
    if num + num1