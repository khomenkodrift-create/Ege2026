ans = []
for x in range(1, 2030):
    num = 5 ** 150 + 5 ** 100 - x
    cnt = 0
    while num:
        if num % 5 == 0: cnt += 1
        num //= 5
    ans.append([cnt, x])
result = max(ans, key=lambda x: (x[0], x[1]))
print(result)