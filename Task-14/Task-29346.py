n = 5 * 1296 ** 2021 - 4 * 216 ** 2022 + 3 * 36 ** 2023 - 2 * 6 ** 2024 - 2025
ans = []
while n > 0:
    x = n % 36
    ans.append(x)
    n //= 36

cnt = 0
for i in ans:
    if i % 2 == 0:
        cnt += 1
print(cnt)