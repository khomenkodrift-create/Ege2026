from itertools import permutations

graph = 'ЕД ДА АГ ГЖ ЖК КВ ВГ ВБ БД ЕБ'.split()
matrix = '358 78 16 57 146 35 248 127'.split()

print(*range(1, 9))
for i in permutations('АБВГДЕЖК'):
    if all(str(i.index(x)+ 1) in matrix[i.index(y)] for x , y in graph):
        print(*i)
        #21