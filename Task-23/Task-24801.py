def f(x, y, c):
    if x > y: return 0
    if x == y: return int(c == 1)
    c += int(x in {24, 32})
    if c > 1: return 0
    return f(x + 1, y, c) + f(x + 2, y, c) + f(x + 4, y, c) + f(x + 8, y, c)

print(f(16, 48, 0))