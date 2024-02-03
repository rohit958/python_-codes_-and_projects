class node:
    def __init__(self):
        self.children={}
        self.end = False

class Trie:
    def __init__(self):
        self.root= node()

    def insert(self,s):
        node=self.root
        for char in s:
            if char not in node.children:
                node.children[char]= node
            node=node.children[char]
        node.end=True

    def search(self,s):
        node=self.root
        for char in s:
            if char not in node.children:
                return False
            else:
                node= node.children[char]
        return node.end
    def prefix(self,startswith):
        node=self.root
        for char in startswith:
            if char not in node.children:
                return False
            node=node.children[char]
            return True


string="Shivani is my love."

MyTrie=Trie()
MyTrie.insert(string)
print(MyTrie.prefix(startswith="Shi"))
print(MyTrie.search("love"))
