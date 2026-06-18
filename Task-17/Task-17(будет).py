with open() as file:
    data = [int(i) for i in file]
min_9 = min(i for i in data if i > 0 and i % 9 == 0)

ans = []
for num1, num2 in zip(data, data[1:]):
    if num1 != num2:
        if abs(num1 - num2) % min_9 == 0:
            ans.append(num1 + num2)
print(len(ans), max(ans))