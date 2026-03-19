from itertools import product, permutations, repeat


def f(w, x, y, z):
    return x and (z <= w) and not y


for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):
    table = [
        (x1, x2, 1, x3, 1),
        (x4, 1, 0, x5, 1),
        (1, 0, x6, x7, 1)
    ]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
             if all(f(**dict(zip(p, t))) == t[-1] for t in table):
                 print(*p, sep='')