def f(x, y):
    return (x >= 27) or (2 * x < 3 * y) or ((x + 2) * (y - 3) < A)

for A in range(0, 1000):
    if all(f(x, y) for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
        break
        #393