# Условный оператор

# num = int(input()) # 5

# if num > 0:
#     print('+')
# elif num < 0:
#     print('-')
# else:
#     print('0')
#
# # Задача на баллы
#
# score = int(input())
#
# if 80 <= score <= 100:
#     print('5')
# elif 60 <= score <= 79:
#     print('4')
# elif 40 <= score <= 59:
#     print('3')
# else:
#     print('на пересдачу')


# Аналог тернарного оператора
# В Cpp: num > 0 ? '+' : '-'
# num = int(input())
# print('+' if num > 0 else '-')

# match case

# mark = int(input())
#
# match mark:
#     case 5:
#         print('от 80 до 100')
#     case 4:
#         print('от 60 до 80')
#     case 3:
#         print('от 40 до 60')
#     case 2:
#         print('от 0 до 40')
#     case _:
#         print('неверная оценка')

# Сложные условия
# Порядок выполнения
# 1. **
# 2. *, /, //, %
# 3. +, -
# 4. ==, !=, >, >=, <, <=
# 5. not
# 6. and - вернет True когда оба условия True
# 7. or - вернет True когда хотя бы одно из условий True
