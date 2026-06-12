def f(current, end):
    if current == end: return 1
    if current < end: return 0
    return f(current - 1, end) + f(current // 2, end)
print(f(30, 8) * f(8, 1))