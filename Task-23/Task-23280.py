def f(current, end):
    if current == end: return 1
    if current < end or current == 8: return 0
    return f(current - 1, end) + f(current - 4, end) + f(current // 3, end)

print(f(19, 14) * f(14, 2))