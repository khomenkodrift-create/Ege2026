with open(r'.\files\17_4622.txt') as file:
    data = [int(i) for i in file]

minn = min(i for i in data if i > 0 and i % 19 == 0)
ans = []
for num1, num2 in zip(data, data[1:]):
    if num1 + num2 < minn:
        ans.append(num1 + num2)
print(len(ans), abs(max(ans))) # abs - модуль