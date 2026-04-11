from itertools import product, permutations, repeat


def f(w, x, y, z):
    return (w == z) or not (y <= w) or not x

for x1, x2, x3, x4, x5 in product((0, 1), repeat= 5):
    table = [
        (0, 0, 1, x1, 0),
        (x2, 1, 1, x3, 0),
        (0, x4, x5, 0, 0)
    ]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if all(f(**dict(zip(p, t))) == t[-1] for t in table):
                print(*p, sep='')
                #ywxz