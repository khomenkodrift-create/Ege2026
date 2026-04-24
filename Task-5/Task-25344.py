from string import printable

def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'
ans = []
for N in range(1, 100000):
    R = convert(N, 3)
    if N % 3 == 0:
        R = R + R[-2:]
    else:
        summ = sum(int(i) for i in str(R)) * 3
        R = R + convert(summ, 3)
    R = int(R, 3)
    if R > 208 and R % 2 == 1:
        ans.append(R)
print(min(ans))