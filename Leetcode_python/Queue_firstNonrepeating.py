from collections import deque
def firstUniqChar( s):
    queue=deque()
    queue.append(s[0])
    index=[]
    for i in range(1,len(s)-2):
        if queue[0]==s[i]:
            queue.popleft()

        if queue[len(queue)-1]==s[i]:
            queue.pop()

        else:
            queue.append(s[i])
            index.append(i-1)

    return index[0]

    print(queue)


s=("loveleetcode")

print(firstUniqChar(s))