def f(n):
    cnt = 0
    while n > 0:
        if n % 6 == 0:
            cnt += 1
        n //= 6
    return cnt

min_zero = float('inf')

for x in range(1, 2030):
    num = 6 ** 2030 + 6 ** 100 - x
    x = f(num)
    if x < min_zero:
        min_zero = x
print(min_zero)