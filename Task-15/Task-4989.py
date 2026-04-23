def DEL(n, m):
    return n % m == 0
def f(x):
    B = 20 <= x <= 80
    A = A1 <= x <= A2
    return B <= (DEL(x, 17) <= A)

for A1 in range(1, 1000):
    for A2 in range(1, 1000):
        if all(f(x) for x in range(1, 1000)):
            print(A2 - A1)
            break
            #34
