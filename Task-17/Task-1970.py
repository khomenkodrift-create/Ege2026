with open(r'.\files\17_1970.txt') as file:
    data = [int(i) for i in file]

def del3(x):
    return x % 3 == 0

rez = []

for i in range(len(data) - 1):
    x1 = data[i]
    x2 = data[i + 1]
    s = x1 + x2
    if del3(x1) + del3(x2) >= 1:
        rez.append(s)

print(len(rez), max(rez))