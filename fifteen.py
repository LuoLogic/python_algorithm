# 究极暴力方法
def threeSumEqualZero(nums):
    List = []
    for f in nums:
        twnums = nums[:]  # 若twnums=nums 复制后新旧列表跟着一起变
        # 使用copy，l=nums.copy
        # 使用切片 l=nums[:]
        # for 循环 l=[i for i in nums]
        twnums.remove(f)
        for tw in twnums:
            thnums = twnums[:]
            thnums.remove(tw)
            for th in thnums:
                if not(f+tw+th):
                    temp = [f, tw, th]
                    List.append(temp)

    for i in range(len(List)):
        List[i] = sorted(List[i], reverse=False)

    for i, key in enumerate(List):
        for k in range(len(List)):
            split = List[i+1::]
            if key in split:
                j = List.index(key, i+1)
                List.pop(j)  # remove是删除是key的元素(从头开始查找key，找到删除)，pop(i)是删除指定位置元素

    return List


def threePoint(nums):
    nums.sort()
    res = []  # 结果列表
    k = 0  # k指向排序后Nums的第一个

    # 外层循环是k，即i和j所指位置的数相加，和k再加，若k>0,则s不可能为0
    # 否则若s<0,则i所指数小了，i++后再比较
    # s>0,则j所指数字大了，j--后再比较
    # 若i或j所指数字和他们的上一个相同，则再i++,j--跳过
    for k in range(len(nums)-2):
        if nums[k] > 0:
            break

        if k > 0 and nums[k] == nums[k-1]:
            continue
        i = k+1
        j = len(nums)-1
        while i < j:
            s = nums[k]+nums[i]+nums[j]
            if s < 0:
                i += 1
                while i < j and nums[i] == nums[i+1]:
                    # 防止排序后连续出现三个相同的数字情况，如nums4
                    if nums[k]+nums[i]+nums[i+1] == 0 and nums[i] != nums[i-1]:
                        res.append([nums[k], nums[i], nums[i+1]])
                    i += 1
            elif s > 0:
                j -= 1
                while i < j and nums[j] == nums[j+1]:
                    j -= 1
            else:
                res.append([nums[k], nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i-1]:
                    i += 1
                while i < j and nums[j] == nums[j+1]:
                    j -= 1

    # res_f = []
    # for i in res:
    #     if i not in res_f:
    #         res_f.append(i)

    return res


def threeSum(nums):
    nums.sort()
    count = len(nums)
    collect = []
    for i in range(count):
        left = i+1
        right = count-1
        # 避免重复找同一个数据
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # 数据按小到大排列，每次选取nums[i]，在其后寻找符合a + b + c = 0的两个数据
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum == 0:
                col = [nums[i], nums[left], nums[right]]
                collect.append(col)
                left += 1
                right -= 1
                # 循环中nums[i]已确定，当再确定1个数时，另一个数也确定，左右端任一端出现重复均可跳过
                while nums[left] == nums[left-1] and left < right:
                    left += 1
                while nums[right] == nums[right+1] and left < right:
                    right -= 1
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
    return collect


nums = [-1, 0, 1, 2, -1, -4]
nums1 = [3, 0, -2, -1, 1, 2]

nums3 = [-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]
nums4 = [-4, -1, -4, 0, 2, -2, -4, -3, 2, -3, 2, 3, 3, -4]

res = []
# res = threeSumEqualZero(nums2)
# res = threeSum(nums4)
res = threePoint(nums4)
print(res)
