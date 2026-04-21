from  itertools import combinations

def f(x):
    P = 23 <= x < 45
    Q = 34 <= x <= 56
    A = A1 <= x <= A2
    return (not A) or (not P) and Q

lineA = [23, 34, 45, 56]
lineX = [23.5, 34.5, 45.5]

ans = []
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans.append(A2 - A1)

print(max(ans))