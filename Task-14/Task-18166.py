def convert(num, sys):
    res = ''
    while num:
        res += str(num%sys)
        num//=sys
    return res[::-1]
ans = []
for x in range(2, 2026):
    num = convert(5**2025 + 5**200 - x, 5)
    ans.append([num.count('4'), x]) # тк по условию узнаем у кого больше 4ок
print(max(ans))#1876 - самый большой х