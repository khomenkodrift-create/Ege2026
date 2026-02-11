ans = []

def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


for N in range(1 , 100_000):
    R = convert(N, 7)
    if N % 7 == 0:
        R = '34' + R.replace('6', '*')
        R = R.replace('3', '6')
        R = R.replace('*', '3')
    else:
        R = '3' + R[1:] + '45'
    R = int(R, 7)
    if R < 2876:
        ans.append([R, N])
ans = sorted(ans, key=lambda x: (x[0], -x[1]))
print(ans[0]) # 6