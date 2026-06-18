from string import printable

for x in printable[:22]:
    num1 = int(f'63{x}89875', 22)
    num2 = int(f'17{x}51', 22)
    num3 = int(f'75{x}3', 22)
    num = num1 + num2 + num3
    if num % 21 == 0:
        print(num // 21)

#или

num = 228

summ = 0
while num:
    if num % 36 > 9: summ += num % 36
    num //= 36

print(summ) #сумма чисел

#или

num = 4*16**25 + 2*8**30 - 64**10
print(bin(num)[2:].count('0'))

num = 4*16**25 + 2*8**30 - 64**10

cnt = 0
while num:
    if num % 2 == 0: cnt += 1
    num //= 2

print(cnt) #кол-во нулей

#или
ans = []
for x in range(1, 2030):
    num = 5 ** 150 + 5 ** 100 - x
    cnt_0 = 0
    while num:
        if num % 5 == 0: cnt_0 += 1
        num //= 5
    ans.append([cnt_0, x])

print(max(ans, key=lambda x:(x[0], -x[1])))