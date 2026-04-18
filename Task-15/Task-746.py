from itertools import combinations

def f(x):
    P = 12 <= x <= 26
    Q = 30 <= x <= 53
    A = A1 <= x <= A2
    return (A <= P) or Q

line_A = [12, 26, 30, 53]
line_X = [20, 27, 32]

ans = []
for A1, A2 in combinations(line_A, 2):
    if all(f(x) for x in line_X): #тождественно истинна (1)
        ans.append(A2 - A1)

print(max(ans))