arr=[1,2,4,6]
arr2=[1,3,4,5,12,45]

arr_new=[]

i=0
j=0

while j<len(arr2):
  if i < len(arr):
    if i < j:
      arr_new.append(arr[i])
      arr_new.append(arr2[j])
    else:
      arr_new.append(arr2[j])
      arr_new.append(arr[i])
  else:
    arr_new.append(arr2[j])
  i+=1
  j+=1
print(arr_new)