'''
Stack  operations
1-Push-insert
2-POP-remove
3-isEmpty
4-isFull
'''
# 1. implement using list
# 2. implement-using collections and using queue.queueLIFO libraries
# 3. implement using Linked list:benefit(now need of continous allocation of memory)
'''
from logging import exception
stack = []

if __name__ == '__main__':
    stack.append("bagha")  # push
    stack.append("jetha lal")
    stack.append("natu kaka")
    stack.append("Iyer Idli")
    print(stack)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    print(stack)


    def isEmpty(l):
        if len(l) == 0:
            raise exception("stack is empty")


    isEmpty(stack)
'''
'''
# using collections
from collections import deque

st = deque()
st.append('Jetha lal')
st.append('Hans raj hathi')
st.append('Tarak Mehta')
st.append('Matka King Mohan lal')

print(st)

print('Popping:',st.pop())
print('Popping:',st.pop())
print('Popping:',st.pop())
print('Popping:',st.pop())

'''

# using linked list

