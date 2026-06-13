with open(r'.\files\17_17558.txt') as file:
    data = [int(d) for d in file]

count_32 = sum(1 for x in data if x % 32 == 0)

ans = []
for i in range(len(data) - 1):
    a, b = data[i], data[i + 1]

    if (a < 0 or b < 0) and (a + b < count_32):
        ans.append(a + b)

print(len(ans), max(ans))