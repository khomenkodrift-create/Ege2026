from itertools import product, permutations, repeat

def f(w, x, y, z):
    return (not (w <= ((x == y) or y))) and (z <= x)

for x1, x2, x3, x4, x5 in product((0, 1), repeat=5):
    table = [
        (x1, 1, 1, x2, 1),
        (0, x3, x4, 0, 1),
        (x5, 0, 1, 0, 1)
    ]
    if len(set(table)) == len(table):
        for p in permutations('wxyz'):
            if all(f(**dict(zip(p, t[:-1]))) == t[-1] for t in table):
                print(*p, sep='')