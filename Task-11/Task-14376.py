from math import ceil, log2
L = 25
N = 10 + 8190
i = log2(N) #спросить втф
I = ceil(L * i / 8)
print(36000 / 200 - I)