def F(current, end):
    if current == end: return 1
    if current > end or current == 17: return 0
    return F(current + 2, end) + F(current + 3, end) + F(current * 2, end)

print(F(3, 10) * F(10, 25))