from itertools import combinations
from math import dist
def center(clr):
    ans = []
    for dot in clr:
        sum_dist =sum(dist(dot, d) for d in clr)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'.\files\27_B_28766 (1).txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append([float(x), float(y)])
        if data[0] == 'Z' and data[2:] == 'I':
            stars.append([float(x), float(y)])

clr_1 = [d for d in dots if d[1] > 22]
clr_2 = [d for d in dots if 22 > d[1] > 16]
clr_3 = [d for d in dots if d[1] < 16]

stars_1 = [s for s in stars if s in clr_1]
stars_2 = [s for s in stars if s in clr_2]
stars_3 = [s for s in stars if s in clr_3]

B1 = []
for d1 in stars_1:
    for d2 in clr_1:
        if d1 != d2:
            B1.append(dist(d1, d2))

for d1 in stars_1:
    for d2 in stars_1:
        if d1 != d2:
            B1.append(dist(d1, d2))

for d1 in stars_1:
    for d2 in stars_1:
        if d1 != d2:
            B1.append(dist(d1, d2))

print(min(B1) * 10000)

print(len(stars_1), len(stars_2), len(stars_3))


cntr_2 = center(clr_2)
cntr_3 = center(clr_3)
B2 = dist(cntr_2, cntr_3)
print(B2 * 10000)

#############################################

cluster_1 = [[d for d in dots if 22 < d[1]],
             [s for s in stars if 22 < s[1]]]
cluster_2 = [[d for d in dots if 16 < d[1] < 22],
             [s for s in stars if 16 < s[1] < 22]]
cluster_3 = [[d for d in dots if d[1] < 16],
             [s for s in stars if s[1] < 16]]
clusters = [cluster_1, cluster_2, cluster_3]

B1 = min(dist(d1, d2) for cluster in clusters for d1, d2 in combinations(cluster[1], 2))
min_center = center(min(clusters, key=lambda x: len(x[1]))[0])
max_center = center(max(clusters, key=lambda x: len(x[1]))[0])
B2 = dist(min_center, max_center)
print(B1 * 10_000, B2 * 10_000)