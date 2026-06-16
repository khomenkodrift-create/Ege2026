with open(r'.\files\17_17636.txt') as file:
    data = [int(i) for i in file]

max_3 = max(i for i in data if str(i)[-1:] == '3' and len(str(abs(i))) == 3)
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = len(str(abs(num1))) == 3 and str(num1)[-1:] == '3'
    u2 = len(str(abs(num2))) == 3 and str(num1)[-1:] == '3'
    u3 = len(str(abs(num3))) == 3 and str(num1)[-1:] == '3'
    if u1 + u2 + u3 >= 1:
        ans.append(num1 + num2)
print(len(ans), max(ans))