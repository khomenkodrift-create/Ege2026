from string import printable
count = 0 # тк будет обнуляться, если включить в if
for y in range(1, 101):  # правая граница не включая (не превышающих 100)
    for x in printable[1:25]: #(тк х в начале)
        num1 = int(f'8AF7{x}11', 25) # f подставляет вместо х
        num2 = int(f'{x}DA87', 25)
        num = num1 + num2
        if num % y == 0:
            count += 1
            break
print(count) #63