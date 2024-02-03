"""
Merge Sort Algorithm
divide and conquer
Space Complexity-
Time Complexity-O(NLog(n))
Worst TimeComplexity= O(log(n^2))
"""

numbers = [54, 26, 93, 17, 77, 31, 44, 55, 20]


def printArray(text, arrray):
    print(text, arrray)


def merge(list1, list2):
    combined = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


def mergeSort(array):
    if len(array)==1:
        return array
    mid=int(len(array)/2)

    fisthalf=mergeSort(array[:mid])
    secondhalf=mergeSort(array[mid:])
    return merge(fisthalf,secondhalf)

if __name__ == '__main__':
    printArray('before sorting: ', numbers)
    #mergeSort(numbers)
    print("sorted array",mergeSort(numbers))

