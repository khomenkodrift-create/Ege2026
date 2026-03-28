from functools import lru_cache

def F(n):
    if n > 400: return n ** n
    return n + 6 + F(n + 12)

print(F(72) - F(108))
#270