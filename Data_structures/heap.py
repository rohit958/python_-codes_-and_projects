# heap
    # STORAGE O(n)
    # AND ACCESS- LOG(n)
    # STRUCTURE- PARENT AND CHILD NODE
    # CAN BE IMPLEMENTED USING LIST AND INDEXING

class Max_heap:
    def __init__(self):
        self.heap=[]

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def heapyfy(self,index):
        left_child_index=self._left_child(index)
        right_child_index=self._right_child(index)
        max_value_index = index

        while True:
            if left_child_index<len(self.heap) and self.heap[left_child_index]>self.heap[index]:
                max_value_index=left_child_index

            if right_child_index< len(self.heap) and self.heap[right_child_index]>self.heap[index]:
                max_value_index=right_child_index

            if max_value_index!= index:
                self._swap(max_value_index,index)
                index=max_value_index
            else:
                return
    def print_heap(self):
        print(self.heap)


    def insert(self,value):
        if len(self.heap)==0:
            self.heap.append(value)

        else:
            self.heap.append(value)
            current=len(self.heap)-1

            if current > 0 and self.heap[current] > self.heap[self._parent(current)]:
                self._swap(current,self._parent(current))
                current=self._parent(current)
        self.heapyfy(0)

    def delete(self):
        if len(self.heap)==0:
            return None
        elif len(self.heap)==1:
            self.heap.pop()
        else:
            self.heap[0]=self.heap.pop()
            self.heapyfy(0)

my_heap= Max_heap()

my_heap.insert(3)
my_heap.insert(1)
my_heap.insert(8)
my_heap.insert(9)
my_heap.insert(4)

my_heap.print_heap()
my_heap.delete()
my_heap.print_heap()