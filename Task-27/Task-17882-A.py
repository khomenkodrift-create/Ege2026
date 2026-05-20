from  math import dist

def center(clr):
    ans = []
    for dot in clr:
        sum_dist = sum(dist(dot, d) for d in clr)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'.\files\27_A_17882.txt') as file:
    dots = [list(map(float, i.split())) for i in file]
clr_1 = [d for d in dots if d[1] > 3]
clr_2 = [d for d in dots if d[1] < 3]


center_1 = center(clr_1)
center_2 = center(clr_2)

Px = (center_1[0] + center_2[0]) / 2
Py = (center_1[1] + center_2[1]) / 2

print(Px * 10000, Py* 10000)