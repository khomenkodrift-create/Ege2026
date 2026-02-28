def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


from string import printable

for x in printable[1:100]:
    num_1 = int(f'7A{x}0123', 100)
    num_2 = int(f'1B{x}A64{x}', 100)
    num_3 = int(f'{x}98012C', 100)
    num = num_1 + num_2 + num_3
    if num % 21 == 0:
        print(convert(num // 21, 6))
