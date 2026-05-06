def f_19(x, y, s):
    if x + y >= 154: return s % 2 ==0
    if s == 0: return False

    h = [
        f_19(x + 4, y, s - 1),
        f_19(x * 3, y, s - 1),
        f_19(x, y + 4, s - 1),
        f_19(x, y * 3, s - 1)
    ]
    return any(h)

print('19)', [x for x in range(1, 142) if f_19(x, 11, 2)])

def f(x, y, s):
    if x + y >= 154: return s % 2 ==0
    if s == 0: return False

    h = [
        f(x + 4, y, s - 1),
        f(x * 3, y, s - 1),
        f(x, y + 4, s - 1),
        f(x, y * 3, s - 1)
    ]
    return any(h) if (s - 1)% 2 == 0 else all(h)

print('20)', [x for x in range(1, 142) if f(x, 11, 3) and not f(x, 11, 1)])
print('21)', [x for x in range(1, 142) if f(x, 11, 4) and not f(x, 11, 2)])
