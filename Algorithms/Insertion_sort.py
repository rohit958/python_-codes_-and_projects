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


def insertion_sort(ar):
    if len(ar) == 0 or len(ar) == 1:
        return ar
    else:
        for i in range(0, len(ar) - 1): #starts from 2nd position and compares element in reverse direction till the correct order found
            for j in range(i + 1, 0, -1):
                if ar[j] < ar[j - 1]:
                    temp = ar[j]
                    ar[j] = ar[j - 1]
                    ar[j - 1] = temp
        return ar


print(insertion_sort([1,2,3,5,4]))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]

 """

