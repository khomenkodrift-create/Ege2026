def f(current, end):
    if current == end: return 1
    if current < end or current == 21: return 0
    return f(current - 1, end) + f(current - 6, end) + f(current // 2, end)
print(f(34, 29) * f(29, 19) * f(19, 6))
