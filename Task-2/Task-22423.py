from itertools import product, permutations, repeat


def f(w, x, y, z):
    return ((z <= x) and (x <= y) or (w == (z or x)))

for x1, x2, x3, x4, x5, x6, x7 in product((0, 1), repeat=7):
    table = [
        (x1, 1, x2, x3, 0),
        (x4, x5, 1, 1, 0),
        (x6, 1, x7, 1, 0)
    ]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if all(f(**dict(zip(p, t))) == t[-1] for t in table):
                print(*p, sep='')