def f(current, end):
    if current == end: return 1
    if current < end or current == 36: return 0
    return f(current - 3, end) + f(current - 6, end) + f(current // 2, end)
print(f(86, 53) * f(53, 12))