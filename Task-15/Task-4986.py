def DEL(n, m):
    return n % m == 0
def f(x):
    B = 50 <= x <= 70
    return DEL(x, A) or DEL(x, 23) <= (not B)

for A in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(A)