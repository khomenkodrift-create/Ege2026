from functools import lru_cache
@lru_cache(None)
def F(n):
    return 3 * (G(n - 2) + 5)
@lru_cache(None)
def G(n):
    if n < 8: return 3 * n
    return G(n - 3) + 2

for i in range(7, 12346):
    G(i)

for i in range(1, 12346):
    F(i)

print(F(12345))

#24750