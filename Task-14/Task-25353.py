ans = []
for x in range(1, 27000):
    num = 3 * 27 ** 9 + 2 * 27 ** 6 + 27 ** 3 - x
    cnt = 0
    while num > 0:
        if num % 27 == 0:
            cnt += 1
        num = num // 27
    if cnt == 6:
        print(x)
