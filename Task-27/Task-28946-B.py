from math import dist

def center(clr):
    ans = []
    for dot in clr:
        sum_dist = sum(dist(dot, d) for d in clr)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'.\files\27_B_28946.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file if len(i.split()) == 2]

clr_1 = [d for d in dots if d[1] > 25]
clr_2 = [d for d in dots if d[1] < 20 and d[0] < 23]
clr_3 = [d for d in dots if d[0] > 25]

cntr_1 = center(clr_1)
cntr_2 = center(clr_2)
cntr_3 = center(clr_3)

