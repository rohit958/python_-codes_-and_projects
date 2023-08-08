from operator import length_hint

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

example:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

'''


def twoSum( nums, target):
        for x in range(len(nums)):
            sum=0
            for y in range(x+1,len(nums)):
                sum = nums[x]+nums[y]
                if sum == target:
                    ans=[]
                    ans.append(x)
                    ans.append(y)
                    return ans
                    break
                else:
                    continue

print(twoSum([2,7,11,15],9))