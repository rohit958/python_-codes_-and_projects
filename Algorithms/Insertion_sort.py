"""
Insertion Sort Algorithm

Space Complexity-
Time Complexity-O(NLog(n))
Worst TimeComplexity= O(log(n^2))
cons-unstable
"""

ar = [54, 26, 93, 17, 77, 31, 44, 55, 20]


def PrintArray(text , arrray):
    print(text, arrray)


def InsertionSort( ar):
    for i in range(len(ar)-1):
        min_indx = i # selection
        for j in range(i+1,len(ar)):  #comparision to find smaller element than selected
            if ar[j]<ar[min_indx]:
                min_indx=j
        if min_indx!=i:
            temp=ar[i]  #swapping
            ar[i]=ar[min_indx]
            ar[min_indx]=temp
    return ar


if __name__ == '__main__':
    PrintArray('before sorting: ', ar)
    InsertionSort(ar)
    PrintArray("after sorting: ", ar)
