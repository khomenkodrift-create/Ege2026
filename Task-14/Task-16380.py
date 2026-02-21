from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]
num = 4*3125**2019 + 3*625**2020 - 2*125**2021 + 25**2022 - 4*5**2023 - 2024
num = convert(num, 25)
count = 0
for i in num:
    if int(i, 25) > 10: # или i > 'a': (таблица аски)
        count += 1 # += прибавляет и сохраняет
print(count)