from itertools import product, permutations

def f(w, x, y, z):
    return ((z == x) <= w) and (w <= (y and x))

for x1, x2, x3 in product((0, 1), repeat=3):
    table = [
        (1, 1, x1, 0, 1),
        (1, x2, x3, 0, 1),
        (1, 0 ,1 , 1, 1)
    ]
    if len(set(table)) == len(table):
        for p in permutations('wxyz'):
            if all(f(**dict(zip(p, t))) == t[-1] for t in table):
                print(*p, sep='')
                #yzxw