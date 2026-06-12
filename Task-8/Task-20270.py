from itertools import product
digits = [0, 1, 2, 3, 4, 5, 6]
even = [0, 2, 4, 6]
odd = [1, 3, 5]
cnt = 0
for p in product(digits, repeat=5):
    if p[0] == 0:
            continue
    mask = "".join(['E' if x in even else 'O' for x in p])
    if 'EEE' not in mask and 'EE' in mask:
        cnt += 1
print(cnt)