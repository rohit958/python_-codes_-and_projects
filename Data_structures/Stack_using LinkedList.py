
class Node:
    def __int__(self,value):
        self.value=value
        self.next=None


class Stack:
    def __init__(self, value):
        NewNode = Node(value)
        self.top = NewNode
        self.height = 1

    def printStack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next


Stack_ex = Stack(6)
Stack_ex.printStack()