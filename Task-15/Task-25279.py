from itertools import combinations
def f(x):
    A = A1 <= x <= A2
    P = 66 <= x <= 67
    Q = 32 <= x <= 125
    T = 30 <= x <= 491
    return (not A) <= (P or (not Q) or (not T))
lineA = [30, 32, 66, 67, 125, 491]
lineX = [30.5, 32.5, 66.5, 67.5, 125.5]
ans = []
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans.append(A2 - A1)
print(min(ans))