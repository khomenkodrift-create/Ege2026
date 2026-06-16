with open(r'.\files\7923.txt') as file:
    data = [list(map(int, i.split())) for i in file]
ans = []
for pos, line in enumerate(data, start=1):
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 3, 3]:
        pov = [i for i in line if line.count(i) != 1]
        nepov = [i for i in line if line.count(i) == 1]
        if sum(pov) / 6 < nepov[0]:
            ans.append(pos)
print(max(ans))