from asyncio import graph
from itertools import permutations

graph = 'АБ БВ ВА ВЕ ЕЖ ЖД ЕД ДГ ГА'.split()
matrix = '25 137 267 56 46 345 23'.split()

print(*range(1, 8))
for i in permutations('АБВГДЕЖ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)