def f(current, end):
    if current == end: return 1
    if current > end or current == 35: return 0
    return f(current + 1, end) + f(current + 2, end) + f(current * 2, end)
print(f(7, 13) * f(13, 15) * f(15, 51))