from itertools import permutations
graph = 'AB BC CD DA AG GD DF DE FE GF'.split()
matrix = '24 14567 67 125 246 235 23'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x , y in graph):
        print(*i)
        print(25 + 22 + 29)
        #76