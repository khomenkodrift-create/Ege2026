print('w x y z')
for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                F = not(y <= x) or (z <= w) or not z
                if not F:
                    print(w, x, y, z)
#yxzw

#или
from itertools import product, permutations, repeat


def f(w, x, y, z):
    return not(y <= x) or (z <= w) or not z

for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):
    table = [
        (x1, 0, x2, x3, 0),
        (0, 1, x4,  x5, 0),
        (1, x6, x7, 0, 0)
    ]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if all(f(**dict(zip(p, t))) == t[-1] for t in table):
                print(*p, sep='')







