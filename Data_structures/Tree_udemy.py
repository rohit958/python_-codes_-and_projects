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
    def BFS(self):
        curr=self.root
        res=[]
        q=[]
        q.append(curr)

        while(len(q)>0):
            curr=q.pop(0)
            res.append(curr.value)
            if curr.Left is not None:
                q.append(curr.Left)
            if curr.Right is not None:
                q.append(curr.Right)
        return res
    def print_Tree(self):
        if self.Left is not None:
            self.print_Tree()
        print(self.root),
        if self.Right is not None:
            self.print_Tree()
    def DFS_preorder(self):
        #preorder- first parent then left then right
        res=[]
        def tranverse(Node):
            res.append(Node.value)
            if Node.Left is not None:
                tranverse(Node.Left)
            if Node.Right is not None:
                tranverse(Node.Right)
        tranverse(self.root)
        return res

    def DFS_postorder(self):
        # postorder- first left then right then parent
        res = []

        def tranverse(Node):

            if Node.Left is not None:
                tranverse(Node.Left)
            if Node.Right is not None:
                tranverse(Node.Right)
            res.append(Node.value)
        tranverse(self.root)
        return res

    def DFS_inorder(self):
        # postorder- first left then parent then right- can be used for sorting
        res = []

        def tranverse(Node):

            if Node.Left is not None:
                tranverse(Node.Left)
            res.append(Node.value)
            if Node.Right is not None:
                tranverse(Node.Right)

        tranverse(self.root)
        return res
MyTree=Tree()

MyTree.insert(4)
MyTree.insert(7)
MyTree.insert(9)
MyTree.insert(1)
MyTree.insert(8)
MyTree.insert(5)

MyTree.insert(6)
MyTree.insert(2)

print("Breadth First Search:",MyTree.BFS())

print("Depth First Search-pre_order:",MyTree.DFS_preorder())

print("Depth First Search-post_order:",MyTree.DFS_postorder())

print("Depth First Search-in_order:",MyTree.DFS_inorder())