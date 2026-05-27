from itertools import combinations
from math import dist

with open(r'.\files\27_B_29081.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append([float(x), float(y)])
        if data != 'VII' and int(data[1]) >= 8:
            stars.append([float(x), float(y)])

clr_1 = [d for d in dots if d[1] < 15]
clr_2 = [d for d in dots if 15 < d[1] < 22]
clr_3 = [d for d in dots if 22 < d[1]]

stars_1 = [s for s in stars if s in clr_1]
stars_2 = [s for s in stars if s in clr_2]
stars_3 = [s for s in stars if s in clr_3]

B1 = []
for d1 in stars_1:
    for d2 in stars_2:
        B1.append(dist(d1, d2))
for d1 in stars_3:
    for d2 in stars_1:
        B1.append(dist(d1, d2))
for d1 in stars_2:
    for d2 in stars_3:
        B1.append(dist(d1, d2))
print(min(B1) * 10_000)


B2 = []
for d1 in stars_1:
    for d2 in stars_1:
        if d1 != d2:
            B2.append(dist(d1, d2))
for d1 in stars_2:
    for d2 in stars_2:
        if d1 != d2:
            B2.append(dist(d1, d2))
for d1 in stars_3:
    for d2 in stars_3:
        if d1 != d2:
            B2.append(dist(d1, d2))
B2 = sum(B2) / len(B2)

### или

B2 = [dist(s1, s2) for s in stars for s1, s2 in combinations(s, 2)]
print(B2 * 10_000)