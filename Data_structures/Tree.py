# Tree implementation using Class
# Tree is Non-liner, Hierarchical Data Structure
# tree works reccursively

class treenode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = treenode("Cars")

    hatchback = treenode("Hatchbacks")
    hatchback.add_child(treenode("i20"))
    hatchback.add_child(treenode("Baleno"))
    hatchback.add_child(treenode("Altroz"))

    sedans = treenode("Sedans")
    sedans.add_child(treenode("City"))
    sedans.add_child(treenode("Verna"))
    sedans.add_child(treenode("Virtus"))

    SUV = treenode("SUVs")
    SUV.add_child(treenode("XUV700"))
    SUV.add_child(treenode("Harrier"))
    SUV.add_child(treenode("WR-V"))


    root.add_child(hatchback)
    root.add_child(sedans)
    root.add_child(SUV)
    root.print_tree()

    return root


if __name__ == '__main__':
    build_product_tree()