def cnt_zero(n):
    cnt = 0
    while n > 0:
        if n % 6 == 0:
            cnt += 1
        n //= 6
    return cnt

min_zero = float('inf')

for x in range(1, 2030):
    val = 6 ** 2030 + 6 ** 100 - x
    cnt_0 = cnt_zero(val)
    if cnt_0 < min_zero:
        min_zero = cnt_0

print(min_zero)