ans = []
for x in range(1, 232):
    num = 64 ** 678 + 55 ** 123 - x
    cnt = 0
    while num > 0:
        if num % 25 == 0:
            cnt += 1
        num //= 25
    ans.append(cnt)
print(max(ans))