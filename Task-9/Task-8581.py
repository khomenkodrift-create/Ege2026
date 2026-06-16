with open(r'.\files\8581.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for line in data:
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 1, 1, 1, 3]:
        pov = [i for i in line if line.count(i) != 1] # повторяющиеся
        nepov = [i for i in line if line.count(i) == 1] # неповторяющиеся
        if sum(nepov) / 4 <= pov[0]:
            print(sum(line))