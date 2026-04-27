def DEL(n, m):
    return n % m == 0
def f(x):
    B = 70 <= x <= 80
    return  DEL(x, 12) and B and (not DEL(x, A))
cnt = 0
for A in range(1, 1000):
    if all(not f(x) for x in range(1, 1000)):
        cnt +=1
print(cnt)