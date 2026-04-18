from itertools import combinations

def f(x):
    P = 10<= x <= 45
    Q = 35 <= x <= 78
    A = A1 <= x <= A2
    return ((not P) <= Q) and not A

line_A = [10, 35, 45, 78]
line_X = [10.5, 35.5, 45.5]
ans = []
for A1, A2 in combinations(line_A, 2):
    if all(not f(x) for x in line_X): # тождественно ложное (0)
        ans.append(A2 - A1)
print(min(ans))