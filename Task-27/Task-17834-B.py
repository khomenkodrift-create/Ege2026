from math import dist
def center(clr):
    ans = []
    for dot in clr:
        sum_dist = sum(dist(dot, d) for d in clr)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'.\files\27_B_17834.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file if len(i.split()) == 2]

clr_1 = [d for d in dots if d[0] < 3 and d[1] > 2]
clr_2 = [d for d in dots if d[0] > 3 and d[1] > 2]
clr_3 = [d for d in dots if d[1] < 2]

cntr_1 = center(clr_1)
cntr_2 = center(clr_2)
cntr_3 = center(clr_3)

Px = (cntr_1[0] + cntr_2[0] + cntr_3[0]) / 3
Py = (cntr_1[1] + cntr_2[1] + cntr_3[1]) / 3

print(Px * 100, Py * 100)

#408, 352