def countPairs( nums, target) :
    pair_cnt = 0
    first_ptr = 0
    last_ptr = len(nums)-1
    nums.sort()
    while first_ptr < last_ptr:
        if (nums[first_ptr] + nums[last_ptr]) < target:
            pair_cnt= pair_cnt + last_ptr-first_ptr
            first_ptr+=1
        else:
            last_ptr-=1
    return pair_cnt


print(countPairs([-6,2,5,-2,-7,-1,3], -2))
