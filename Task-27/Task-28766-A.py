from math import dist
def center(clr):
    ans = []
    for dot in clr:
        sum_dist = sum(dist(dot, d) for d in clr)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'.\files\27_A_28766.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append([float(x), float(y)])
        if data[0] == 'Y' and data[2:] == 'III':
            stars.append([float(x), float(y)])

clr_1 = [d for d in dots if d[1] < 10]
clr_2 = [d for d in dots if d[1] > 10]

#print(len(clr_1), len(clr_2)) - минимальное расстояние

cntr_1 = center(clr_1)
cntr_2 = center(clr_2)

A = []
for s in stars:
    A.append(dist(cntr_2, s))

print(min(A) * 10000, max(A)* 10000)

###########################################

cluster_1 = [d for d in dots if d[1] < 10]
cluster_2 = [d for d in dots if d[1] > 10]
clusters = [cluster_1, cluster_2]

min_center = center(min(clusters, key=len))
A = [dist(min_center, s) for s in stars]
print(min(A) * 10_000, max(A) * 10_000)