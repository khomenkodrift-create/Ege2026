num = 15625**16 - 3125**3 * 25**19 + 625**4 - 2005
cnt_0 = 0
while num:
    if num % 5 ==0:
        cnt_0 += 1
    num //= 5

print(cnt_0)
#38