from itertools import permutations

graph = 'HD DA AC CB BH HF FE EG GC GA'.split()
matrix = '368 34 126 27 67 35 458 17'.split()

print(*range(1, 9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
        #28