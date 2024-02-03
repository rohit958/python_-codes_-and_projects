"""
Selection Sort Algorithm

Space Complexity-
Time Complexity-O(n^2)
Worst TimeComplexity= O(n^2)
"""

num = [54, 26, 93, 17, 77, 31, 44, 55, 20]


def PrintArray(text, arrray):
    print(text, arrray)


def selsort(ar):
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
    PrintArray('before sorting: ', num)
    selsort(num)
    PrintArray("after sorting: ", num)
