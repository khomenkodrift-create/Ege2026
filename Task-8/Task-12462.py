from itertools import combinations, product
from string import printable
range_ = range(16)
val_3 = len(list(combinations(range_, 3)))
val_5 = len(list(combinations(range_, 5)))

print(val_3 + val_5)

#или

cnt = 0
for a in printable[:16]:
    for b in printable[:16]:
        for c in printable[:16]:
            if a > b > c:
                cnt += 1
for a in printable[:16]:
    for b in printable[:16]:
        for c in printable[:16]:
            for d in printable[:16]:
                for e in printable[:16]:
                    if a > b > c > d > e:
                        cnt += 1
print(cnt)