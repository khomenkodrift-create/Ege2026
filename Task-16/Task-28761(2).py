from functools import lru_cache
@lru_cache(None)
def F(n):
    if n < 10: return 3
    return (n + 4) * F(n - 5)

for i in range(1, 257488):
    F(i)

print((F(257487) / 683 + 67 * F(257477)) / F(257472))