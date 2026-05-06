from itertools import combinations
def f(x):
    B = 22 <= x <= 40
    C = 32 <= x <= 50
    A = A1 <= x <= A2
    return (not A) <= (B == C)

lineA = [22, 32, 40, 50]
lineX = [22.5, 32.5, 40.5]
ans = []
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans.append(A2 - A1)
print(min(ans))