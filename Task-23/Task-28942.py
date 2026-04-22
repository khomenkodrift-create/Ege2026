def f(current, end):
    if current == end: return 1
    if current < end or current == 73: return 0
    return f(current - 3, end) + f(current - 8, end) + f(current // 2, end)

print(f(76, 41) * f(41, 12))

#80