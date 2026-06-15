from itertools import product, permutations, repeat


def f(w, x, y, z):
    return (not (x == (w and (not z)))) and (y == (x and (not w)))

for x1, x2, x3, x4, x5, x6 in product((0, 1), repeat=6):
    table = [
        (x1, x2, 0, x3, 1),
        (x4, 0, x5, 0, 1),
        (0, x6, 1, 0 , 1)
    ]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if all(f(**dict(zip(p, t))) == t[-1] for t in table):
                print(*p, sep='')