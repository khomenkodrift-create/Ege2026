ans = []

def convert(num, sys):
    res = ''
    while num:
        res += str(num, sys)
        num //= sys
    return res[::-1]

for N in range(1, 100_000):
    if N % 5 == 0:
        R = convert(N, 5)
        R =  '33' + R.replace('1', '*')
        R.replace('4', '1')
    else:
        R = R.replace(
    if R > 1922:
        ans.append(N)

print(min(ans))