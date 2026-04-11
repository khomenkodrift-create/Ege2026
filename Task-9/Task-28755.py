with open(r'9_28755.ods') as file:
    data = [list(map(int, i.split())) for i in file]

print(data)