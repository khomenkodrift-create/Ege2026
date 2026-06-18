def DEL(n, m):
    return n % m == 0
def f(x):
    B = 70 <= x <= 90
    return DEL(x, A) or (B <= (not(DEL(x, 16))))

for A in range(1, 10000):
    if all(f(x) for x in range(1, 10000)):
        print(A) #80