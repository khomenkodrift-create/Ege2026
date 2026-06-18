with open(r'.\files\task-9.txt') as file:
    data = [list(map(int, i.split())) for i in file]
ans = []
for pos, line in enumerate(data, start=1):
    if len(line) == len(set(line)):
        if (max(line) + min(line)) * 2 > sum(line) - max(line) - min(line):
            ans.append(pos)
print(min(ans))
