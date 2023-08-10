"""
binary search
"""


def search(nums,target):
    low = 0
    end = len(nums)-1
    mid = (low+end) // 2
    while low <=end:
        if nums[mid] < target:
            low=mid+1
            mid = (low+end) // 2
        elif nums[mid] > target:
            end =mid-1
            mid = (low + end) // 2
        else:
            return mid
print(search([5],5))