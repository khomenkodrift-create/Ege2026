from itertools import combinations

def f(x):
    P = 12 <= x <= 28
    Q = 15 <= x <= 30
    A = A1 <= x <= A2

    return (P <= A) and (not Q or A)
lineA = [12, 15, 28, 30]
lineX = [12.5, 15.5, 28.5]

ans = []

for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans.append(A2 - A1)

print(min(ans))