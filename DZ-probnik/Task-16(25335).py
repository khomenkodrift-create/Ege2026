from functools import lru_cache
@lru_cache(None)
def F(n): #672 -> 18
    if n >= 19: return F(n - 4) + 3580
    return 6 * (G(n - 7)- 36)
@lru_cache(None)
def G(n):
    if n >= 248045: return n/20 + 28
    return G(n + 9) - 4

for i in range(248047, 12, -1):
    G(i)

for i in range(673, 18, -1):
    F(i)

print(F(673))