def removeDuplicates( nums) -> int:
    if len(nums) == 0:
        return 0
    else:
        if len(nums) == 0:
            return 0
        else:
            a = 1
            for pos in range(1, len(nums)):
                if nums[pos] != nums[pos - 1]:
                    nums[a] = nums[pos]
                    a += 1
            return a
nums = [0,1,1,1,2,2,3,3,4]

print(removeDuplicates(nums))