n = 15 * 49**237 + 37 * 343**500 - 14 * 7**35
cnt = 0
while n > 0:
    x = n % 49
    if x > 15:
        cnt += 1
    n //= 49
print(cnt)