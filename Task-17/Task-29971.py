with open(r'.\files\17_29971 (1).txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data)