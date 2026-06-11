def f(current, end):
    if current == end: return 1
    if current > end: return 0
    return f(current + 3, end) + f(current * 2, end)
print(f(3, 27) * f(27, 63))