from itertools import permutations

graph = 'AB BD DC AD AC CE AE CF EF CG GF'.split()
matrix = '25 135 24567 37 1236 357 346'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)asdas