with open(r'.\files\17_2473.txt') as file:
    data = [int(i) for i in file]
ans = []
for nums in zip(data, data[1:]):
    if sum(num % 7 == 0 for num in nums) >= 1:
        if sum(str(num)[-1:] == '3' for num in nums) >= 1:
            ans.append(sum(nums))
print(len(ans), min(ans))