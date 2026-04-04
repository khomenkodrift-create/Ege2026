from itertools import permutations, repeat

graph = 'BE EF FA AD DB BC EC CA'.split()
matrix = '36 456 145 236 23 124'.split()

print(*range(1, 7))
for i in permutations('ABCDEF'):
    if all(str(i.index(x)+ 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
        # 26 + 18 = 44



from itertools import permutations
graph = ''.split()
matrix = ''.split()

print(*range(1, x))
for i in permutations('АЛФАВИТ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)


from itertools import product, permutations

def f(w, x, y, z):
    return sfghfgh

for x1, x2, x3, x4 in product((0,1), repeat=4):
    table = [
        (),
        (),
        ()
    ]
    len(set(table)) == len(table)
    for p in permutations('wxyz'):
        if all(f(**dict(zip(p, t))) == t[-1] for t in table):
            print(*p, )