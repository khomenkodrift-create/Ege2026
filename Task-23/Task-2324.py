def f(current, end):
    if current > end:return 0
    if current == end:return 1
    num = str(current)
    if num[1] < num[2]:
        repl_current = int(num[0] + num[2] + num[1])
        return f(repl_current, end) + f(current + 1, end)
    else:
        return f(current + 1, end)


print(f(101, 154))