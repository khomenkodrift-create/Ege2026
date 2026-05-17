with open(r'.\files\17_23376.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if len(str(abs(i))) == 5 and str(i)[-2:] == '37')
ans = []
for nums in zip(data, data[1:]):
    if sum(len(str(abs(num))) == 5 for num in nums) == 1:
        if sum(nums) ** 2 < maxx ** 2:
            ans.append(sum(nums))
print(len(ans), max(ans))