def convert(num, sys):
    res = ''
    while num:
        res = str(num % sys)
        num //= sys
    return res[::-1]
num = 5*216**3031 + 4*36**3042 - 3*6**3053 - 3064
print(sum(map(int,convert(num, 6)))) # 5

# или
num = 5*216**3031 + 4*36**3042 - 3*6**3053 - 3064
cnt = 0
while num:
    cnt = num % 6
    num //= 6
print(cnt)