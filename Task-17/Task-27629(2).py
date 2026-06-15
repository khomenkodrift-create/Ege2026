with open(r'.\files\17_27629.txt') as file:
    data = [int(i) for i in file]

max_43 = max(i for i in data if str(i)[-2:] == '43' and len(str(abs(i))) == 4)
ans = []
for num1, num2 in zip(data, data[1:]):
    u1 = len(str(abs(num1))) == 4
    u2 = len(str(abs(num2))) == 4
    kvadrat = (num1 + num2) ** 2
    if u1 + u2 >= 1 and kvadrat < max_43 ** 2:
        ans.append(kvadrat)
print(len(ans), max(ans))