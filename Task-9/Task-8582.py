with open(r'.\files\8582.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 1, 1, 1, 3]:
        if line.count(max(line)) == 1:
            cnt += 1
print(cnt)