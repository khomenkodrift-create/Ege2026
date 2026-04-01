def f(current, end):
    if current == end: return 1
    if current < end: return 0
    return f(current - 1, end) + f(current // 2, end)

print(f(40, 16) * f(16, 6))

#60