def containsNearbyDuplicate( nums, k):
    anchor = 0
    mid = len(nums) // 2
    Flag = False
    while anchor <= mid:
        dist = 0
        for x in range(anchor + 1, len(nums)):
            if nums[anchor] == nums[x]:
                dist = abs(anchor - x)
        if dist != 0 and dist < k:
            Flag = True
            return Flag
        anchor += 1
    return Flag


print(containsNearbyDuplicate(nums=[1,2,3,1],k=2))