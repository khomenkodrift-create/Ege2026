from itertools import permutations, product, repeat

def f(w, x, y, z):
    return (w == z) or not(y <= w) or not x

for x1, x2, x3, x4, x5 in product((0, 1), repeat=5):
    table = [
        (x1, 0, 1, 0, 0),
        (x2, 1, 1, x3, 0),
        (0, x4, x5, 0, 0)
    ]
    if len(set(table)) == len(table):
        for p in permutations('wxyz'):
            if all(f(**dict(zip(p, t))) == t[-1] for t in table):
                print(*p, sep='')
                #zwxy