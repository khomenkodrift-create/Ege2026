from itertools import product

# Алфавит семеричной системы
digits = [0, 1, 2, 3, 4, 5, 6]
even = [0, 2, 4, 6]
odd = [1, 3, 5]

count = 0

# Перебираем все возможные пятизначные последовательности
for p in product(digits, repeat=5):
            # Число не может начинаться с нуля
    if p[0] == 0:
            continue

            # Создаем строку-маску, где 'E' - четная цифра, 'O' - нечетная
    mask = "".join(['E' if x in even else 'O' for x in p])

            # Условия:
            # 1. 'EEE' не должно быть в маске (никакие три четные не стоят рядом)
            # 2. 'EE' должно быть в маске (хотя бы одна пара четных рядом)
    if 'EEE' not in mask and 'EE' in mask:
        count += 1
print(count)