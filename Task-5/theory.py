# Стандартные системы счисления
# Двоичная система
num = 20

print(bin(num)[2:]) # str
# или
print(f'{num:b}')

# Восьмеричная система

print(oct(num)[2:])
# или
print(f'{num:o}')

# Шестнадцатеричная система

print(hex(num)[2:])
# или
print(f'{num:x}')

# Перевод в любую систему счисления (2 <= sys <= 9)

# def convert(num, sys): #
#     res = ''
#     while num: # можно не писать != 0, тк только тру и фолс понимает, а когда 0 = фолс
#         res += str(num % sys)
#         num //= sys
#     return res[::-1]

# print(convert(20, 2))
#
# convert()

# Перевод в любую систему счисления (2 <= sys <= 36)
from string import printable

def convert(num, sys):
    res = ''
    while num: # можно не писать != 0, тк только тру и фолс понимает, а когда 0 = фолс
        res += printable[num % sys]
        num //= sys
    return res[::-1]

# Полезные алгоритмы
# Сумма цифр двоичной системы
num_bin = '10101'
print(num_bin.count('1'))
# Сумма цифр любой системы (2 <= sys <= 9)
print(sum(map(int, num_bin)))
# Сумма цифр любой системы (2 <= sys <= 36)
print(sum(map(lambda x: int(x, 36), num_bin)))
