k=3

arr= [1,2,0,64,53,3,0,32,534,0,32,53]

max_sum=0
sub_array=[]

for x in range(0,len(arr)-k+1):
    window = arr[x:x+k]
    if sum(window) > max_sum:
        max_sum = sum(window)
        sub_array = window
print(sub_array)