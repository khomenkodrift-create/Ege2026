from itertools import combinations
range_ = range(16)
val_3 = len(list(combinations(range_, 3)))
val_5 = len(list(combinations(range_, 5)))

print(val_3 + val_5)