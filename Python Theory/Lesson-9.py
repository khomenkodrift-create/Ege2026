# Цикл while

num = 0
while num < 5:
    # print('hello')
    num += 1

# Сумма цифр числа
num = 123
summ = 0
while num:
    summ += num % 10
    num //= 10  # num = num // 10
# print(summ)

# Цикл for

# range(n) - диапазон от 0 до n не включительно
# range(m, n) - формирует диапазон чисел от n до m не включительно с шагом 1
# range(n, m, k) - формирует диапазон чисел от n до m не включительно с шагом k

for i in range(6, 1, -1):
    print(i)


