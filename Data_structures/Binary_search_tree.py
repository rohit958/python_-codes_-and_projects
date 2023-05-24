class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def in_order_transversal(self):
        elements =[]
        # visit left tree
        if self.left:
            elements += self.left.in_order_transversal()

        # visit root node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_transversal()

        return elements

    def search(self,val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def Calculate_sum(self):
        pass

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left.delete(val)

        elif val > self.data:
            if self.right:
                self.right.delete(val)

        else:
            if self.left is None and self.right is None:
                return None

            elif self.left is None:
                return self.right

            elif self.right is None:
                return self.left

        min_val= self.right.find_min()
        self.data =min_val
        self.right = self.right.delete(min_val)

        return self

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range (len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    Countries = ["INDIA","PAKISTAN","USA","CANADA","UK","ISRAEL","SRI LANKA","AUSTRALIA","UKRAINE","ARGENTINA"]
    Countries_tree = build_tree(Countries)
    print(Countries_tree.in_order_transversal())

    Countries_tree.delete("UK")
    print("after removing-UK:",Countries_tree.in_order_transversal())




