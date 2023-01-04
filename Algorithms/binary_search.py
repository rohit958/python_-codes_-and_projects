'''
Binary search using iteration
time complexity-O(log(n^2))
space complexity-O(1)
works best with sorted array
'''

import array as arr
numbers=arr.array('i',[1,2,3,4,5,6,7,45,66,77])#already sorted array

def binary_search(element):
    low=0
    high=len(numbers)-1
    mid=(low+high)//2

    
    while low <= high:
        if numbers[mid]<element:
            low=mid+1
            mid=(low+high)//2

        elif numbers[mid]>element:
            high=mid-1   
            mid= (low+high)//2
        else:
            return mid
    return -1
 
if __name__=="__main__":
    ele=int(input("give anumber to search:"))

    res=binary_search(ele)
    if res==-1:
        print (ele, "not found in array")          
    else :
        print (ele," found in array, at index :", res  )

