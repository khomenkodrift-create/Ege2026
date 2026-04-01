def f(current, end):
    if current == end: return 1
    if current > end or current == 56: return 0
    return  f(current + 3, end)  + f(current + 7, end) + f(current * 3, end)

print(f(12, 40) * f(40, 72)* f(72, 89))