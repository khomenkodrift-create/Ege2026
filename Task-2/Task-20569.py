from itertools import permutations, product


def f(w, x, y, z):
    return ((w <= z) == (x <= (not y))) and (x or z)

for x1, x2 in product((0, 1), repeat=2):
    table = [
        (1, 0, 0, 1, 1),
        (1, 1, 1, 0, 0),
        (0, x1, 0, x2, 1)
    ]
    if len(set(table)) == len(table):
        for p in permutations('wxyz'):
            if all(f(**dict(zip(p, t))) == t[-1] for t in table):
                print(*p, sep='')