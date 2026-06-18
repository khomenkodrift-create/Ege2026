with open(r'.\files\31116.txt') as file:
    data = [list(map(int, i.split())) for i in file]
ans = []
for pos, line in enumerate(data):
    if len(line) == len(set(line)):
        if (max(line) + min(line)) * 2 > sum(line) - min(line) - max(line):
            ans.append([pos, sum(line)])
print(min(ans))