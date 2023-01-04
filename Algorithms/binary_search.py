import array as arr

numbers=arr.array('i',[1,2,3,4,5,6,7,77,54,66,45])

def binary_search(element):
    low=0
    mid=int(len(numbers)/2)
    high=len(numbers)

    for x in numbers:
        if numbers[x]<numbers[mid]:
            



    
       
if __name__=="__main__":
    ele=int(input("give anumber to search:"))

    res=binary_search(ele)
    if res==-1:
        print (ele, "not found in array")          
    else :
        print (ele," found in array, at index :", res+1  )