#two sum - get the pairs whose sum is 10

# two pointers
arr=[1,2,6,7,3,4,7,5,9]

arr.sort()

target=10

i=0
j=len(arr)-1
result=[]

while i<j:           
    if (arr[i]+arr[j])==target:
        result.append([arr[i],arr[j]])
        i+=1
        j-=1
    elif (arr[i]+arr[j]) < target:
        i += 1
    else:
        j -= 1
print(result)


