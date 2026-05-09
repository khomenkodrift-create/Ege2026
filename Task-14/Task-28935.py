from string import printable

for x in printable[:23]:
    num_1 = int(f'761{x}035', 23)
    num_2 = int(f'338{x}932', 23)
    num = num_1 + num_2
    if num % 22 == 0:
        print(int(num // 22))