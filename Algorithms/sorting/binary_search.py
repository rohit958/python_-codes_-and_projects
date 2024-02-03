'''
Binary search using iteration-Divide and conquer
time complexity-O(log(n))
space complexity-O(1)
works best with sorted array

'''

import array as arr
numbers=[-1,0,3,5,9,12]#already sorted array
33

def binary_search(arr,element):
    low=0
    high=len(arr)-1
    while low<=high:
        mid = (high + low) // 2
        if arr[mid]== element:
            return mid
        elif arr[mid]>element:
            high=mid-1
        elif element > arr[mid]:
            low=mid+1
    return -1

 
if __name__=="__main__":
    ele=int(input("give anumber to search:"))

    res=binary_search(numbers,ele)
    if res==-1:
        print (ele, "not found in array")          
    else :
        print (ele," found in array, at index :", res  )

