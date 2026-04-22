def f(x, y):
    return (2 * x + y != 70) or (x < y) or (A < x)
for A in range(1, 1000)[::-1]: #если максимальное
    if all(f(x, y) for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
        break
        #23