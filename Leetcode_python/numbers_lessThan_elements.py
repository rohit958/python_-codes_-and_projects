def smallerNumbersThanCurrent(nums):
    sortedn=sorted(nums)
    res=[]
    for i in nums:
        res.append(sortedn.index(i))
    print(res)
    return res


nums=[8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))