"""
Merge Sort Algorithm

Space Complexity-
Time Complexity-O(NLog(n))
Worst TimeComplexity= O(log(n^2))
"""

numbers = [54, 26, 93, 17, 77, 31, 44, 55, 20]


def printArray(text, arrray):
    print(text, arrray)


def mergeSort(ar):
    if len(ar) <= 1:
        return ar
    mid = int(len(ar) / 2)
    left = ar[:mid]
    right = ar[mid:]
    mergeSort(left)
    mergeSort(right)
    mergeSortedArrays(left, right, ar)


def mergeSortedArrays(a, b, arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0
    while i < len_a and j < len_b:
        if a[i] < + b[j]:
            arr[k] = a[i]
            i += 1

        else:
            arr[k] = b[j]
            j += 1
        k += 1
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


if __name__ == '__main__':
    printArray('before sorting: ', numbers)
    mergeSort(numbers)
    printArray("after Merge sorting: ", numbers)
