num = 4**36 + 3*4**20 + 4**15 + 2*4**7 + 49
num = hex(num)[2:]
print(len(set(num))) #5