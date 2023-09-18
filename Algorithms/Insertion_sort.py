"""
Insertion Sort Algorithm

Space Complexity-
Time Complexity-O(NLog(n))
Worst TimeComplexity= O(log(n^2))
"""

ar = [54, 26, 93, 17, 77, 31, 44, 55, 20]


def PrintArray(text , arrray):
    print(text, arrray)


def InsertionSort( ar):
    for i in range(len(ar)-1):
        min_inx = i
        for j in range(i+1,len(ar)-1):



if __name__ == '__main__':
    PrintArray('before sorting: ', ar)
    InsertionSort(ar)
    PrintArray("after sorting: ", ar)
