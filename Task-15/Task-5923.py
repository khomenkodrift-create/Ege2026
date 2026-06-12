from itertools import combinations

def f(x, A1, A2):
    P = 5 <= x <= 280
    Q = 295 <= x <= 400
    R = 375 <= x <= 450
    A = A1 <= x <= A2
    return (Q <= P) or ((not A) <= R)
lineA = [5, 280, 295, 375, 450]
lineX = [5.5, 280.6, 295.5, 375.5]

ans = []

for A1, A2 in combinations(lineA, 2):
    if all(f(x, A1, A2) for x in lineX):
        ans.append(A2 - A1)
print(min(ans))