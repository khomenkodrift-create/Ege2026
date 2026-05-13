with open(r'.\files\17_4597.txt') as file: # точка выводит нас из текущего файла
    data = [int(i) for i in file] # int для работы со строками как с числами

minn = min(i for i in data if i > 0)
ans = []
for num1, num2 in zip(data, data[1:]):
    u1 = num1 % 117 == minn
    u2 = num2 % 117 == minn
    if u1 + u2 >= 1: # будет считать 1 + 1 = 2 тк u1 - true и u2 - true, >= 1 - хотя бы одного из элементов
        ans.append(num1 + num2)
print(len(ans), max(ans))