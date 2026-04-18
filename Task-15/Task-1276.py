from itertools import combinations

def f(x):
    P = 15 <= x <= 33
    Q = 35 <= x <= 48
    A = A1 <= x <= A2
    return (A and not Q) <= (P or Q)

lineA = [15, 33, 35, 48]
lineX = [15.5 , 33.5, 35.5]

ans = []
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans.append(A2 - A1)

print(max(ans))