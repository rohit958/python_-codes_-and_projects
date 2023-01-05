'''
Bubble sort 

time complexity-
space complexity-


'''

import numpy as np


numbers=np.array([44,2,23,5,66,97,6,2,1])

def BubbleSort(ar):
    temp=0
    for i in range(len(ar)-1):
        for j in range(len(ar)-1):
            if ar[j]>ar[j+1]:
                temp=ar[j]
                ar[j]=ar[j+1]
                ar[j+1]=temp
                


def PrintArray(arrray):
    print(arrray)


if __name__=='__main__':
    PrintArray(numbers)
    SortedArray=arr.array('i',[BubbleSort(numbers)])
    PrintArray()