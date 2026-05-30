from string import printable
for x in printable[:29]:
    num_1 = int(f'463{x}7921', 29)
    num_2 = int(f'8241{x}153', 29)
    num = num_1 + num_2
    if num % 28 == 0:
        print(num // 28)