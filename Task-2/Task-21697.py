from itertools import product, permutations, repeat


def F(w, x, y, z):
    return not(x <= y) or (z==w) or z

for x1, x2, x3, x4, x5, x6, x7 in product((0, 1), repeat=7):
    table = [
        (0, 0, x1, x2, 0),
        (x3, x4, 1, x5, 0),
        (x6, 1, 0, x7, 0)
    ]

    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if all(F(**dict(zip(p, t))) == t[-1] for t in table):
                print(*p, sep='')
                #zyxw