def numIdenticalPairs(nums) -> int:
    result = {}
    res = 0
    for i in nums:
        if i in result:
            res += result[i]
            result[i] += 1
        else:
            result[i] = 1

    return res

print(numIdenticalPairs([1,2,3,1,1,3]))