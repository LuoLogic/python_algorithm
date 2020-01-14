def twoSum(nums, target):
    lens = len(nums)
    j = -1
    for i in range(lens):
        if target-nums[i] in nums:
            if ((nums.count(target - nums[i]) == 1) & (target - nums[i] == nums[i])):
                continue
            else:
                j = nums.index(target-nums[i], i+1)
                break

    if j > 0:
        return[i, j]
    else:
        return []


def twoSum1(nums, target):
    map = {}
    for i, num in enumerate(nums):
        complement = target-nums[i]
        if complement in map:
            return map[complement], i

        else:
            map[num] = i


nums = [2, 11, 15, 7]
target = 9
print(nums.count(14))
res = []
res = twoSum(nums, target)
print(res)
re = []
re = twoSum1(nums, target)
print(re)
