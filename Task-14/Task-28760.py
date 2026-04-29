n = 2 * 2187 ** 567 + 729 ** 566 - 2 * 243 ** 565 + 81 ** 564 - 2 * 27 ** 563 - 6561
ans = []
while n > 0:
    x = n % 27
    ans.append(x)
    n //= 27

cnt = 0
for i in ans:
    if i > 9 and i % 2 == 0:
        cnt += 1
print(cnt)
