from string import printable
for x in printable[:16]:
    num1 = int(f'8569{x}', 16)
    num2 = int(f'12{x}48', 16)
    num = num1 + num2
    num_8 = oct(num)[2:]
    c = num_8.count('0') + num_8.count('2') + num_8.count('4') + num_8.count('6')
    # или    cnt = sum(num_8.count(i) for i in '0246')
    if c <= 2:
        print(num_8) #2275735



