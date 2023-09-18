'''
Queue  operations {FIFO}
1-Enqueue
2-Dequeue
3-isEmpty
4-isFull

ways to implement using -using libraries, using linked list,using list
'''


'''
#using list
Q = []

Q.insert(0, 'Raju')
Q.insert(1, 'Shayam')
Q.insert(2, 'Babu Rao')
Q.insert(3, 'Nanji Bhai')
Q.insert(4, 'Tiwari Seth')

print(Q)
print(Q.pop(), '. After Dequeue:', Q)
print(Q.pop(), '. After Dequeue:', Q)
print(Q.pop(), '. After Dequeue:', Q)
'''
# implementing using collections library
'''
from collections import deque

qe = deque()

qe.appendleft( 'Jetha lal')
qe.appendleft('Roshan Singh Sodhi')
qe.appendleft( 'Iyer Idli')
qe.appendleft( 'Popat lal')

print(qe)
print(qe.pop())
print(qe.pop())
'''