def F(current, end):
    if current == end: return 1
    if current < end: return 0
    return F(current - 1, end) + F(current - 3, end) + F(current // 3, end)
print(F(22, 2))