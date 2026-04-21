from itertools import combinations

def f(x):
    P = 13 <= x <= 19
    Q = 17 <= x <= 23
    A = A1 <= x <= A2
    return (not ((not P) <= Q)) <= (A <= ((not Q) <= P))

lineA = [13, 17, 19, 23]
lineX = [13.5, 17.5, 19.5]

ans = []
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans.append(A2 - A1)
print(max(ans))