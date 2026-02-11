ans = []

for N in range(1, 100_000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = R.replace('0', '1')
    else:
        R = '1' + R[1:].replace('1', '00') # 1 оторвали, и назад вернули
    R = int(R, 2)
    if R <= 600:
        ans.append([R, N])

print(max(ans)) # получаем [512, 257] , но в ответ 257 (максимальное N при максимальном R)