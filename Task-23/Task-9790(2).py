def F(current, end):
    if current == end: return 1
    if current < end or current == 9 or current == 16: return 0
    return F(current - 1, end) + F(current - 2, end) + F(current // 3, end)

print(F(19, 3))