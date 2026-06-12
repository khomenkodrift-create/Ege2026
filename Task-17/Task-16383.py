with open(r'.\files\17_16383.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data)
ans = []
for nums in zip(data, data[1:]):
    if sum(len(str(abs(num))) == 5 and str(abs(num))[-2:] == '21' for num in nums) == 1:
        if nums[0] ** 2 + nums[1] ** 2 >= maxx ** 2:
            ans.append(sum(nums))
print(len(ans), max(ans))