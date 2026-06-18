from functools import lru_cache


@lru_cache(None)
def F(n):
    if n == 1: return 1
    if n > 1: return n * F(n - 1)
for i in range(1, 3240):
    F(i)
print((F(3238) // 2 + F(3237)) / F(3236))