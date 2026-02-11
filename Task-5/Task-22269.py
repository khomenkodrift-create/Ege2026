ans = []

def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for N in range(1, 100_000):
    R = convert(N, 5)
    if N % 5 == 0:
        R =  '33' + R.replace('1', '*')
        R = R.replace('4', '1')
        R = R.replace('*', '1')
    else:
        R = '3' + R[1:] + '42'
    R = int(R, 5)
    if R < 1922:
        ans.append([R, N])
ans = sorted(ans,key=lambda x: (-x[0], x[1]))

print(ans[0]) # 9