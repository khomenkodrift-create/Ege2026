with open(r'.\files\17_25356.txt') as file:
    data = [int(i) for i in file]
ans = []
maxx = max(i for i in data if str(i)[-2:] == '30')
for nums in zip(data, data[1:], data[2:]):
    if sum(len(str(abs(num))) != 4 for num in nums) == 1:
        if sum(nums) > maxx:
            ans.append(sum(nums))

print(len(ans), max(ans))