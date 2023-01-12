'''
Stack  operations
1-Push
2-POP
3-isEmpty
4-isFull
'''
# implement using list
# other ways to implement-using collections and using queue.queueLIFO libraries


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
        if(l.pop) is None:
            raise exception("stack is empty")
    isEmpty(stack)

