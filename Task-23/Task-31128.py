def f(cur, end):
    if cur == end: return 1
    if cur > end: return 0
    cur_str = str(cur)
    if int(cur_str[-2]) < int(cur_str[-1]):
        return f(cur + 1, end) + f(int(cur_str[:-2] + cur_str[-1] + cur_str[-2]), end)
    else:
        return f(cur + 1, end)
print(f(100, 150))



def f(cur, end):
    if cur == end: return 1
    if cur > end: return 0
    cur_str = str(cur)
    if int(cur_str[-2]) < int(cur_str[-1]):
        return f(cur + 1, end) + f(int(cur_str[:-2] + cur_str[-1] + cur_str[-2]), end)
    else:
        return f(cur + 1, end)
print(f(100, 150))



cur_str = str(cur)
if int(cur_str[-2]) < int(cur_str[-1]):
    return f(cur + 1, end) + f(int(cur_str[:-2] + cur_str[-1] + cur_str[-2]), end)
else:
    return f(cur + 1, end)







