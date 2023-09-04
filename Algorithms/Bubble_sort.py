#Bubble sort
#con- slow in large dataset
#time complexity-O(log(n^2))
#space complexity-O(1)

#import numpy as np


numbers=[44,2,23,5,66,97,6,2,1]

def BubbleSort(ar):
    swapped=False
    for i in range(len(ar)-1):
        for j in range(len(ar)-1):
            if ar[j]>ar[j+1]:
                temp=ar[j]
                ar[j]=ar[j+1]
                ar[j+1]=temp
                swapped=True
        if swapped==False:
            break
    return ar
                


def PrintArray(arrray):
    print(arrray)


if __name__=='__main__':
    PrintArray(numbers)
    SortedArray=BubbleSort(numbers)
    PrintArray(SortedArray)