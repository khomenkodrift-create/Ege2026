from itertools import product, permutations, repeat


def f(w, x, y, z):
    return not(not(z <= y) or (x == w) or x)

for x1, x2, x3, x4, x5, x6, x7 in product((0,1), repeat=7):
    table = [
        (0, 0, x1, x2, 1),
        (x3, x4, 1, x5, 1),
        (x6, 1, 0, x7, 1)
    ]
    if len(set(table)) == len(table):
        for p in permutations('wxyz'):
            if all(f(**dict(zip(p, t))) == t[-1] for t in table):
                print(*p, sep='')
adsad

