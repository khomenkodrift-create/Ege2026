def f(current, end):
    if current == end: return 1
    if current > end or current == 18 or current == 30: return 0
    return f(current + 1, end) + f(current * 3, end) + f(current * 5, end)
print(f(2, 90))
