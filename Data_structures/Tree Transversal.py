#BST
# smaller value goes to left and grater goes to right
    # tree transversal:
    #                   1.BFS- queue implementation
    #                   2.DFS- stack implelementation

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
            return True
        else:
            temp=self.root

            while (True):
                if NewNode.value == temp.value:
                    return False
                if NewNode.value < temp.value:
                    #left insertion
                    if temp.Left is None:
                        temp.Left=NewNode
                        return True
                    else:
                        temp=temp.Left
                else:
                    # Right insertion
                    if temp.Right is None:
                        temp.Right=NewNode
                        return True
                    else:
                        temp=temp.Right

    def contains(self,value):
        temp=self.root
        while(temp is not None):
            if value < temp.value:
                temp=temp.Left
            elif value > temp.value:
                temp=temp.Right
            else:
                return True
        return False


MyTree=Tree()

MyTree.insert(4)
MyTree.insert(7)
MyTree.insert(9)
MyTree.insert(1)
MyTree.insert(8)
MyTree.insert(5)
MyTree.insert(6)
MyTree.insert(2)