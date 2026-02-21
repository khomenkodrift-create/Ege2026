def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for x in range(1, 2031):
    num = convert(7**170 + 7**100 - x, 7)
    if num.count('0') == 71:
        ans.append(x)
print(max(ans))#2090