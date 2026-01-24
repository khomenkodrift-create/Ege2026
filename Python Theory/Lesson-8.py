# Подключение дополнительных модулей / библиотек
#
# # Стандартный вызов библиотеки
# import math
# print(math.sqrt(9))
#
# # Вызов библиотеки через псевдоним
# import math as m
# print(m.sqrt(9))
#
# # Подключение одной команды из библиотеки
# from math import sqrt
# print(sqrt(9))
#
# # Подключение одной команды из библиотеки через псевдоним
# from math import sqrt as s
# print(s(9))

# Подключение нескольких команд из библиотеки через псевдоним
from math import sqrt as s, log2 as l
# print(s(9))

# Полезные функции из math

from math import *  # подключение всех команд из библиотеки

print(ceil(4.1))  # округление вверх
print(floor(4.9))  # округление вниз
print(sqrt(4))  # квадратный корень
print(log(8, 2), log2(4), log10(100))  # логарифмы
print(pi, e)  # const
