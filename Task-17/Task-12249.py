with open(r'.\files\17_12249.txt') as file:
    data = [int(i) for i in file]
ans = []
maxx = max(i for i in data if len(str(abs(i))) == 5 and str(i)[-1:] == '3')


for nums in zip(data, data[1:], data[2:]):
    if sum(str(num)[-1:] == '3' for num in nums) == 1:
        if sum(nums) < maxx:
            ans.append(sum(nums))
print(len(ans), max(ans))

#1610 - неправильно 99081 - правильно