#heapsort
#steps- 1. build heap
      # 2. delete one by one- O(NlogN)

# heapyfy-similaright_child_indexto sink down

#

array=[9,45,23,53,62,2,5,77,99,522,42,62,45]


def heapify(arr, n, i):
    # Find max_value_index among root and children
    max_value_index = i
    left_child_index= 2 * i + 1
    right_child_index= 2 * i + 2

    if left_child_index< n and arr[i] < arr[left_child_index]:
        max_value_index = left_child_index

    if right_child_index< n and arr[max_value_index] < arr[right_child_index]:
        max_value_index = right_child_index

    # If root is not max_value_index, swap with max_value_index and continue heapifying
    if max_value_index != i:
        arr[i], arr[max_value_index] = arr[max_value_index], arr[i]
        heapify(arr, n, max_value_index)
def heapSort(heap):

       list_len=len(heap)
       for i in range (list_len//2,-1,-1):
              heapify(heap,list_len,i)
       for i in range(list_len-1,0,-1):
              heap[i],heap[0]=heap[0],heap[i]
              heapify(heap,i,0)
       return heap




print(array)

print("array afteright_child_indexsorting:",heapSort(array))





















