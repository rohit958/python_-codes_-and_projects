def removeElement( nums, val) :
    while x in nums:
        nums.pop(x)
    return len(nums)

nums=[3,2,2,3]
val=3

print(removeElement(nums,val))