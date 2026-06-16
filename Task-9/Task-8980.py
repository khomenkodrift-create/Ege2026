with open(r'.\files\8980.txt') as file:
    data = [list(map(int, i.split())) for i in file]
ans = []
for pos, line in enumerate(data, start=1):
    if len(set(line)) == len(line):
        if max(line) - min(line) == sum(line) - max(line)- min(line):
            ans.append(pos)
print(min(ans))