num = 2 * 2187 ** 567 + 729 ** 566 - 2 * 243 ** 565 + 81 ** 564 - 2 * 27 ** 563 - 6561
ans = []
while num > 0:
    x = num % 27
    ans.append(x)
    num //= 27

cnt = 0
for n in ans:
    if n > 9 and n % 2 == 0:
        cnt += 1
print(cnt)