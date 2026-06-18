from itertools import permutations

graph = 'AH HE ED DG GA AF FG DC CB EB BH'.split()
matrix = '234 148 18 127 67 578 456 236'.split()

print(*range(1,9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
        print(21 + 2)