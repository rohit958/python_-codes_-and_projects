def leftRightDifference(nums):
    i=0
    res=[]
    while i < len(nums):
        leftSum = 0
        RightSum = 0

        if i == 0:
            leftSum = 0
        else:
            for y in range(i, 0, -1):
                leftSum += nums[y-1]
        if i < len(nums):
            for x in range(i, len(nums)-1):
                RightSum += nums[x+1]
        else:
            RightSum = 0
        res.append(abs(leftSum - RightSum))
        i += 1
    return res

nums=[10,4,8,3]

print(leftRightDifference(nums))