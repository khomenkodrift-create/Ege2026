from math import dist
def center(clr):
    ans = []
    for dot in clr:
        sum_dist = sum(dist(dot, d) for d in clr)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'.\files\27_B_17915.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file if len(i.split()) == 2]

clr_1 = [d for d in dots if d[0] < 12 and d[1] > 16]
clr_2 = [d for d in dots if d[0] < 15 and d[1] < 9]
clr_3 = [d for d in dots if d[0] > 15 and d[1] < 11]
clr_4 = [d for d in dots if d[0] > 23 and d[1] > 15]

cntr_1 = center(clr_1)
cntr_2 = center(clr_2)
cntr_3 = center(clr_3)
cntr_4 = center(clr_4)

Px = (cntr_1[0] + cntr_2[0] + cntr_3[0] + cntr_4[0]) / 4
Py = (cntr_1[1] + cntr_2[1] + cntr_3[1] + cntr_4[1]) / 4

print(Px * 10000, Py * 10000)
#163215, 128141