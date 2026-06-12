
def f(current, end):
    if current == end: return 1
    if current > end: return 0
    return f(current + 1, end) + f(current + 2, end) + f(current + 3 , end)

print(f(5, 7) * f(7, 11))