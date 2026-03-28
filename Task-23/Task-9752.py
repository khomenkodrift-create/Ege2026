def f(current, end):
    if current == end: return 1
    if current > end or current == 17: return 0
    return f(current + 2, end) + f(current + 3, end) + f(current * 3, end)

print(f(3, 10) * f(10, 25))