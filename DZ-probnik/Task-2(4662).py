from itertools import product, permutations

def f(w, x, y, z):
    return w <= ((x <= z) <= y)

for x1, x2, x3, x4, x5, x6, x7 in product((0, 1), repeat=7):
    table = [
        (x1, x2, 0, 1, 0),
        (x3, 0, 1, x4, 0),
        (x5, x6, x7, 0, 0)
    ]
    if len(set(table)) == len(table):
        for p in permutations('wxyz'):
            if all(f(**dict(zip(p, t))) == t[-1] for t in table):
                print(*p, sep='')