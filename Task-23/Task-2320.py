def f(current, end):
    if current == end: return 1
    if current < end or current == 13: return 0
    return  f(current - 1, end) + f(current - 2, end) + f(current // 3, end)

print(f(19, 6) * f(6, 4))