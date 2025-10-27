#consider a sorted array:
arr = [1, 2, 2, 3, 4, 4, 4, 5, 6]
#remove duplicates using two pointers

left = 0
right = 1

while right < len(arr):
    if arr[left] == arr[right]:
        arr.pop(right)
    else:
        left += 1
        right += 1

print(arr)

arr2 = [1, 2, 2, 3, 4, 4, 4, 5, 6]

seen=set()

for num in arr2:
    if num not in seen:
        seen.add(num)
    # else skip the duplicate 
print(seen)