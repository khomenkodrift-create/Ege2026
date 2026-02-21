from string import printable
for x in printable[:16]:
    num1 = int(f'8569{x}', 16)
    num2 = int(f'12{x}48', 16)
    num = num1 + num2
num_8 = oct(num)[2:]



