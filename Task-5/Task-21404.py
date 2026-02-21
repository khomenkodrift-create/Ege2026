ans = []
for N in range(1, 100_000):
    R = bin(N)[2:]
    if R.count('1') % 2 ==0: # сумма цифр в двоичной записи
        R = '10' + R[2:] + '0'
    else:
        R = '11' + R[2:] + '1'
    R = int(R, 2)
    if R > 480:
        ans.append(N)
print(min(ans)) #176
