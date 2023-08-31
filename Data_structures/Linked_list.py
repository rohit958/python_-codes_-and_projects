# linked list

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Linked_list:
    length=0
    def __init__(self,value):
        New_node=Node(value)
        self.head=New_node
        self.tail=New_node
        self.length=1

    def print_list(self):
        if self.length ==0:
            print("linked list is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.value)
                temp = temp.next


    def append(self,value):
        # adding value at last
        New_node = Node(value)
        if self.length==0:
            self.head=New_node
            self.tail=New_node
        else:
            self.tail.next=New_node
            self.tail=New_node
        self.length+=1

    def pop(self):
        # removes last element
        if self.length==0:
            return None
        else:
            temp=self.head
            pre=self.head
            while (temp.next):
                pre=temp
                temp=temp.next
            self.tail=pre
            self.tail.next=None
            self.length-=1
            if self.length==0:
                self.head=None
                self.tail=None
            return temp
    def prepend(self):
        # add elemnt at beginning
        temp=self.head.next
        self.head=temp

    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp= self.head
            self.head =self.head.next
            temp.next=None
            self.length -= 1

        if self.length == 0:
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return True

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp
