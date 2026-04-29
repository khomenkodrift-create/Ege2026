from itertools import combinations


def f(x):
    P = 25 <= x <= 64
    Q = 40 <= x <= 115
    A = A1 <= x <= A2
    return P <= ((Q and (not A)) <= (not P))
lineA = [25, 40, 64, 115]
lineX = [25.5, 40.5, 64.5]

for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        print(A2 - A1)
        break
        #39