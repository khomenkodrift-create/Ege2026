from math import dist

def center(clr):
    ans = []
    for dot in clr:
        sum_dist = sum(dist(dot, d) for d in clr)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'.\files\27_B_29074.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append([float(x), float(y)])
        if data[0] == 'L' and data[2:] == 'V':
            stars.append([float(x), float(y)])

clr_1 = [d for d in dots if d[1] > 24]
clr_2 = [d for d in dots if d[1] < 24 and d[0] < 18]
clr_3 = [d for d in dots if d[1] < 15]

cntr_1 = center(clr_1)
cntr_2 = center(clr_2)
cntr_3 = center(clr_3)

stars_1 = [s for s in stars if s in clr_1]
stars_2 = [s for s in stars if s in clr_2]
stars_3 = [s for s in stars if s in clr_3]

ans = []

for s in stars_1:
    ans.append(dist(cntr_1, s))

for s in stars_2:
    ans.append(dist(cntr_2, s))

for s in stars_3:
    ans.append(dist(cntr_3, s))


B1 = min(ans)
B2 = max(ans)
print(B1 * 10000, B2 * 10000)

#1738, 20765