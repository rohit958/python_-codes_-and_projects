def removeDuplicates(nums) :
    for pos in range(len(nums) - 1):
        if len(nums) == 0:
            return 0
        else:
            a = 0
            for pos in range(len(nums) - 1):
                if nums[pos] == nums[pos + 1]:
                    a += 1
    return a

print(removeDuplicates( [0,0,1,1,1,2,2,3,3,4]))