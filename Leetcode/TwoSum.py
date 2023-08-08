from operator import length_hint


def twoSum( nums, target):
        for x in range(len(nums)):
            sum=0
            for y in range(x+1,len(nums)):
                sum = nums[x]+nums[y]
                if sum == target:
                    ans=[]
                    ans.append(nums[x])
                    ans.append(nums[y])
                    return ans
                    break
                else:
                    continue

print(twoSum([2,7,11,15],9))