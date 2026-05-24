from math import dist
def center(clr):
    ans = []
    for dot in clr:
        sum_dist = sum(dist(dot, d) for d in clr)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'.\files\27_A_29074.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append([float(x), float(y)])
        if data[0] == 'Z':
            stars.append([float(x), float(y)])

clr_1 = [d for d in dots if d[1] > 10]
clr_2 = [d for d in dots if d[1] < 10]

cntr_1 = center(clr_1)
cntr_2 = center(clr_2)

stars_in_clr1 = [s for s in stars if s[1] > 10]
stars_in_clr2 = [s for s in stars if s[1] < 10]

cnt_1 = len(stars_in_clr1)
cnt_2 = len(stars_in_clr2)

A1 = min(cnt_1, cnt_2)
A2 = max(cnt_1, cnt_2)

print(A1)
print(A2)