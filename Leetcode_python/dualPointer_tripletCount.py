
def arithmeticTriplets( nums, diff) :

    triplet_count = 0
    left = 0
    mid = 1
    right = 2
    length = len(nums)

    while right < length:
        while nums[right] - nums[mid] > diff and mid < right:
            mid = mid + 1

        while nums[mid] - nums[left] > diff and left < mid:
            left += 1

        if nums[mid] - nums[left] == diff and nums[right] - nums[mid]==diff:
            triplet_count += 1
        right += 1
    return triplet_count


print("result",arithmeticTriplets([4,5,6,7,8,9], 2))

