class Node:
  def __init__(self,value):
    self.val=value
    self.next=None

class Queue:
  def __init__(self,value):
    NewNode=Node(value)
    self.first=NewNode
    self.last=NewNode
    self.length=1

  def print_queue(self):
    temp=self.first
    while temp:
      print(temp.val)
      temp=temp.next

  def enqueue(self,value):
    NewNode = Node(value)
    if self.length==0:
      self.first=NewNode
      self.last=NewNode

    else:
      self.last.next=NewNode
      self.last=NewNode
    self.length+=1

  def dequeue(self):
    if self.length==0:
      return None
    if self.length==1:
      self.first=None
      self.lastNone

    else:
      temp=self.first
      self.first=self.first.next
      temp.next=None
    self.length-=1
    return print('removed',temp.val)
MyQueue=Queue(5)
MyQueue.print_queue()
print('after enqueue')
MyQueue.enqueue(6)
MyQueue.enqueue(8)
MyQueue.enqueue(9)
MyQueue.print_queue()
MyQueue.dequeue()
MyQueue.dequeue()
print('after dequeue')
MyQueue.print_queue()