def DEL(n, m):
    return n % m == 0

def f(x):
    B = 15 <= x <= 30
    return DEL(x, A) or (DEL(x, 23) <= (not B))

for A in range(1, 1_000)[::-1]:
    if all(f(x) for x in range(1, 1_000)):
        print(A)
        break