def f(current, end):
    if current == end: return 1
    if current > end or current == 8: return 0
    return  f(current + 1, end) + f(current * 2, end) + f(current * 5, end)
print(f(2, 27) * f(27, 54))