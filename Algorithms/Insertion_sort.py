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
    end = len(ar)
    for i in range(1, end):
        anchor = ar[i]
        j = i-1
        while j >=0 and anchor < ar[j]:
            ar[j+1] = ar[j]
            j -= 1
        ar[j+1] = anchor


if __name__ == '__main__':
    PrintArray('before sorting: ', ar)
    InsertionSort(ar)
    PrintArray("after sorting: ", ar)
