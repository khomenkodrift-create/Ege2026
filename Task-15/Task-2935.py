def f(x, y):
    return (2 * y + 3 * x != 135) or (y > A) or (x > A)

for A in range(0, 1000)[::-1]:
    if all(f(x, y) for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
        break
