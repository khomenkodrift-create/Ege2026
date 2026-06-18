from itertools import product, permutations

def f(w, x, y, z):
    return (x <= y) and (y <= z) and (z <= w)

for x1, x2, x3, x4, x5 in product((0, 1), repeat=5):
    table = [
        (0, x1, x2, 1, 1),
        (1, x3, 0, 1, 1),
        (x4, 1, x5, 0, 1)
    ]
    if len(set(table)) == len(table):
        for p in permutations('wxyz'):
            if all(f(**dict(zip(p, t))) == t[-1] for t in table):
                print(*p, sep='')