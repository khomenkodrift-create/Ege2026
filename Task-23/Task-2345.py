def f(current, end):
    if current == end: return 1
    if current < end: return 0
    return f(current - 1, end) + f(current - 3, end) + f(current // 3, end)

print(f(22,2))