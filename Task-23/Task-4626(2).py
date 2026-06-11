def F(current, end):
    if current == end: return 1
    if current < end: return 0
    return F(current - 2, end) + F(current // 2, end)
print(F(28, 10) * F(10, 1))