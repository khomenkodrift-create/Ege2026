def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


ans = []
for N in range(1, 100_000):
    R = convert(N, 5)
    if len(R) % 2 == 0:
        mid_1 = len(R) // 2
        R = R[mid_1:] + R[:mid_1]
    else:
        R = R + str(N % 5)
        mid_2 = len(R) // 2
        R = R[mid_2:] + R[:mid_2]
    R = int(R, 5)
    if R > 50:
        ans.append(N)
print(min(ans))asdad
