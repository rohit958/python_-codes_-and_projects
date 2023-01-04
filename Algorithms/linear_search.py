import array as arr

numbers=arr.array('i',[1,2,3,4,5,6,7,77,54,66,45])

def linear_search(element):
    for x in numbers:
        if numbers[x]==element:
            return x
    return -1
    
       
if __name__=="__main__":
    ele=int(input("give anumber to search:"))

    res=linear_search(ele)
    if res==-1:
        print (ele, "not found in array")          
    else :
        print (ele," found in array, at index :", res+1  )
        
