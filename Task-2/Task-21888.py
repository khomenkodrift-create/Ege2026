from itertools import product, permutations

def f(w, x, y, z):
    return (x and not y) or (y == z) or w

for x1, x2, x3, x4 in product((0, 1), repeat=4):
    table = [
        (x1, x2, 1, x3, 0),
        (0, 0, 0, 1, 0),
        (1, 0, x4, 1, 0)
    ]
    if len(set(table)) == len(table):
        for p in permutations('wxyz'):
            if all(f(**dict(zip(p, t))) == t[-1] for t in table):
                print(*p, sep='')
                #xwzy