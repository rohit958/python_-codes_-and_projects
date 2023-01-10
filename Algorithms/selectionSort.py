"""
Selection Sort Algorithm

Space Complexity-
Time Complexity-O(n^2)
Worst TimeComplexity= O(n^2)
"""

num = [54, 26, 93, 17, 77, 31, 44, 55, 20]


def PrintArray(text, arrray):
    print(text, arrray)


def selsort(num):
    for x in range(len(num)-1):
        min_index = x
        for j in range(min_index + 1, len(num)):
            if num[j] < num[min_index]:
                min_index = j
        num[x], num[min_index] = num[min_index], num[x]  # 1 line swapping


if __name__ == '__main__':
    PrintArray('before sorting: ', num)
    selsort(num)
    PrintArray("after sorting: ", num)
