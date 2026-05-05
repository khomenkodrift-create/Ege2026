from itertools import product, permutations


def f(w, x, y, z):
    return (not(x <= y)) and ((not(y == z)) <= w)

for x1, x2, x3, x4, x5, x6 in product((0, 1), repeat=6):
    table = [
        (x1, 0, x2, 0, 1),
        (1, x3, x4, 1, 1),
        (x5, 1, x6, 1, 1)
    ]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if all(f(**dict(zip(p, t))) == t[-1] for t in table):
                print(*p, sep='')
                #xzywsfs