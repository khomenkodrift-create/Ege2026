from math import dist
def center(clr):
    ans = []
    for dot in clr:
        sum_dist = sum(dist(dot, d) for d in clr)
        ans.append([sum_dist, dot])
    return min(ans)[1]
with open(r'.\files\27_A_29080.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append([float(x), float(y)])
        if data != 'VII' and data[0] == 'L' and data[1] == '3':
            stars.append([float(x), float(y)])

clr_1 = [d for d in dots if d[1] > 10]
clr_2 = [d for d in dots if d[1] < 10]

cntr_1 = center(clr_1)
cntr_2 = center(clr_2)

stars_1 = [s for s in stars if s in clr_1]
stars_2 = [s for s in stars if s in clr_2]

A1 = []
for d1 in stars:
    A1.append(dist(d1, cntr_1))
print(max(A1) * 10000)

A2 = []
for d2 in stars:
    A2.append(dist(d2, cntr_2))
print(max(A2) * 10000)