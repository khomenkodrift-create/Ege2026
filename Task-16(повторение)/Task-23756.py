from functools import lru_cache


@lru_cache(None)
def G(n):
    if n < 10: return 2 * n
    return G(n - 2) + 1
for i in range(1, 15548):
    G(i)
def F(n):
    return G(n - 2) + 1
print(F(15548))