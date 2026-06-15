with open(r'.\files\17_29349.txt') as file:
    data = [int(i) for i in file]
ans = []
min_123 = min(i for i in data if abs(i) % 123 == 0 and i > 0)
for num1, num2 in zip(data, data[1:]):
    if num1 + num2 < min_123:
        ans.append(num1 + num2)

print(len(ans), max(ans))
