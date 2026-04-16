def f_19(x, y, s):
    if x * y >= 516: return s % 2 ==0
    if s == 0: return False
    h = [f_19(x + 3, y, s - 1),
         f_19(x + 13, y,  s - 1),
         f_19(x , y + 3, s - 1),
         f_19(x, y + 13, s - 1)
         ]
    return any(h)

def f(x, y, s):
    if x * y >= 516: return s % 2 ==0
    if s == 0: return False
    h = [f(x + 3, y, s - 1),
         f(x + 13, y,  s - 1),
         f(x , y + 3, s - 1),
         f(x, y + 13, s - 1)
         ]
    return any(h)  if (s - 1) % 2 == 0 else all(h)
print('19)', [x for x in range(1, 74) if f(x, 7, 2)])
print('20)', [x for x in range(1, 74) if f(x, 7, 3) and not f(x, 7, 1)])
print('21)', [x for x in range(1, 74) if f(x, 7, 4) and not f(x, 7, 2)])