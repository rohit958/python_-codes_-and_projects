#BST
# smaller value goes to left and grater goes to right

class Node:
    def __init__(self,value):
        self.value=value
        self.Left=None
        self.Right=None

class Tree:
    def __init__(self):
        self.root=None

    def insert(self,value):
        NewNode = Node(value)
        if self.root is None:
            self.root=NewNode
        else:
            if value < 