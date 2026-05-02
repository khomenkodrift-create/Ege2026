from itertools import permutations

graph = 'АБ ВГ ВБ ДК ДЕ ЕК ЕГ ВЕ ВД БД'.split()
matrix = '27 1567 67 5 246 2357 1236'.split()

print(*range(1, 8))
for i in permutations('АБВГДЕК'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
        #9