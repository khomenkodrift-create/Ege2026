with open(r'.\files\17_31124.txt') as file:
    data = [int(i) for i in file]
ans = []
minn = min(i for i in data if i > 0 and i % 33 == 0)

for num1, num2 in zip(data, data[1:]):
    if num1 != num2 and abs(num1 - num2) % minn == 0:
        ans.append(num1 + num2)

print(len(ans), max(ans))