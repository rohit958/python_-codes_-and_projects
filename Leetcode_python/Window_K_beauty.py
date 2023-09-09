def divisorSubstrings(num, k):
    nums = str(num)
    if len(nums) == 1:
        return num
    result=0

    for i in range(len(nums)-k+1):
        temp = (nums[i:i+k])
        window= int(temp)

        if window==0:
            continue

        if num % window==0:
            result+=1
        i+=1
    return result

print(divisorSubstrings(430043, 2))
