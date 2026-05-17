with open(r'.\files\17_2473.txt') as file:
    data = [int(i) for i in file]

minn = min(i for i in data if i % 7 == 0 and str(i)[-1:] == '3')
ans = []
for nums in zip(data, data[1:]):
    if sum(len(str(abs(num))) == 5 for num in nums) == 1:
        if sum(nums) < minn:
            ans.append(sum(nums))
print(len(ans), min(ans))

#неверно