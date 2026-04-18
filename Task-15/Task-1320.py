from itertools import combinations

def f(x):
    P = 10 <= x <= 25
    Q = 15 <= x <= 30
    R = 25 <= x <= 40
    A = A1 <= x <= A2
    return (Q <= (not R)) and (A and not P)

lineA = [10, 15, 25, 30, 40]
lineX = [10.5, 15.5, 25.5, 30.5]

ans = []
for A1, A2 in combinations(lineA, 2):
    if all(not f(x) for x in lineX):
        ans.append(A2 - A1)

print(max(ans))