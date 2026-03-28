from itertools import product
cnt = 0
for val in product('0123456789', repeat=6):
    val = ''.join(val)
    left = val[:3]
    right = val[3:]
    if sum(map(int, left)) == sum(int(i) for i in right):
        if len(set(left)) == len(set(right))== 3:
            if any(i in left for i in right):
                if left != right:
print(cnt)