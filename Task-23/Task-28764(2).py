def f(current, end):
    if current == end: return 1
    if current > end or current == 7: return 0
    return f(current + 1, end) + f(current + 3, end) + f(current * 2, end)

print(f(2, 15) * f(15, 25))