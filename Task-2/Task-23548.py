from itertools import product, permutations

def f(w, x, y, z):
    return ((x or y) <= z ) or (y == w) or z
for x1, x2, x3, x4 in product((0, 1), repeat=4):
    table = [
        (0, 1, x1, x2, 0),
        (1, x3, 1, 0, 0),
        (x4, 1, 1, 0, 0)
    ]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if all(f(**dict(zip(p, t))) == t[-1] for t in table):
                print(*p, sep='')
                #wyxz