def f(current, end):
    if current == end: return  1
    if current < end: return 0
    return f(current - 2, end) + f(current // 2, end)

print(f(28, 10) * f(10, 1))