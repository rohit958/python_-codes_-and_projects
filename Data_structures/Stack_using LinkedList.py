
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

    def push(self,value):
        NewNode=Node(value)

        if self.height==0:
            self.top=NewNode

        else:
            NewNode.next=self.top
            self.top=NewNode
        self.height+=1

    def Pop(self):
        if self.height==0:
            return None
        else:
            temp=self.top
            self.top=self.top.next
            temp.next=None
            self.height-=1
        return (print("removed",temp.value))


Stack_ex = Stack(6)
Stack_ex.printStack()