# linked list

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
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

    def set_value(self, index, value):
        if index < 0 or index > self.length:
            return False
        node = self.get(index)
        node.value = value
        return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next=new_node

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after=temp.next
        before=None
        for i in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print('LL before reverse():')
my_linked_list.print_list()

my_linked_list.reverse()

print('\nLL after reverse():')
my_linked_list.print_list()



