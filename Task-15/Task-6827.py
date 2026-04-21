from itertools import combinations

def f(x):
    P = 257 <= x <= 1000
    Q = 5 <= x <= 100
    R = 99 <= x <= 258
    A = A1 <= x <= A2
    return (A <= R) and ((not (A <= P)) <= Q)

lineA = [5, 99, 100, 257, 258, 1000]
lineX = [5.5, 99.5, 100.5, 257.5, 258.5]

ans = []
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans.append(A2 - A1)
print(min(ans))