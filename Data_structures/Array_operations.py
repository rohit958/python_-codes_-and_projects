'''
Array  operations
1-transersal
2-insertion
3-deletion
4-reverse
5-search
6-sort

'''

array=[33,1,5,66,7,9,21,76,88,43]
size=len(array)

def transversal(arr):
    print("transersal")
    for x in range(size):
        print(array[x],end=' ')


def insertion(arr,element,index):
    # if inserted at starting or in mid
    temp=[]
    if index ==0:
        temp [0]=element
        for x in arr :
            temp [x+1]= arr[x]

    elif index< size-1:
        for x in arr:
            temp[x]=arr[x]
            if x == index:
                temp[x]= element
            elif x > index:
                temp[x+1]=arr[x]
    else:
        #if index is at end
        arr.append(element)

    return temp

    

def deletion(arr, element, index):
    # if deletetion is at end

    # if deletion is at starting
    pass



def reverse(arr):
    temp=[]
    for x in reversed(range(size)):
        arr[x]=temp.append(x)

    return temp




if __name__=='__main__':
    transversal(array)
