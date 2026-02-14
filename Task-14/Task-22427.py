from string import printable

for x in printable[:14]:         # несмотря на то что 2 системы, берем меньшую
    num1 = int(f'4b3{x}1C7', 14)
    num2 = int(f'5{x}g83f7', 17)  # но тут всегда берем те системы, которые в условии
    num = num1 + num2
    if num % 15 ==0:
        print(num // 15) #11401190