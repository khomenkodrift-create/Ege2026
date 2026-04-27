def f(x, y):
    return (78125 != y + 4 * x) or (A > x) and (A > y)

for A in range(0, 100000):
    if all(f(x, 78125- 4 * x) for x in range(1, 19531)):
        print(A)
        break