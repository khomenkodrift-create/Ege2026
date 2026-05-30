from itertools import product, permutations, repeat


def f(w, x, y, z):
    return not (w <= (x == y)) and (z <= x)
for x1, x2, x3, x4, x5 in product((0, 1), repeat=5):
    table = [
        (x1, 0, 1, 0, 1),
        (0, x2, x3, 0, 1),
        (x4, 1, 1, x5, 1)
    ]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if all(f(**dict(zip(p, t))) == t[-1] for t in table):
                print(*p, sep='')