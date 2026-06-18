with open() as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 1, 2, 3]:
        pov = [i for i in line if line.count(i) != 1]
        nepov = [i for i in line if line.count(i) == 1]
        if max(pov) < max(nepov):
            cnt += 1
print(cnt)

#или
with open() as file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in enumerate(data, start=1):
    if len(line) == len(set(line)):
        if (max(line) + min(line)) * 2 > sum(line) - max(line) - min(line):
            print(pos)
            break


