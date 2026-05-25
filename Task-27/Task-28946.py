from math import dist
def center(clr):
    ans = []
    for dot in clr:
        sum_dist = sum(dist(dot, d) for d in clr)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'.\files\27_A_28946.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file if len(i.split()) == 2]

clr_1 = [d for d in dots if d[1] > 15]
clr_2 = [d for d in dots if d[1] < 15]

#print(len(clr_1), len(clr_2))
cnt = 0
for i in clr_1:
    if i[1] < center(clr_1)[1]:
        cnt += 1

print(cnt)

cntr_1 = center(clr_1)
cntr_2 = center(clr_2)
A2 = abs(cntr_1[0] - cntr_2[0])

print(A2 * 10000)