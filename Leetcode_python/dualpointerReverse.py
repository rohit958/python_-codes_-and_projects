def reverseStringself( s) :
    leftpointer = 0
    rightpointer = len(s) - 1
    while leftpointer <= rightpointer:
        temp = ""
        temp=s[leftpointer]
        s[leftpointer] = s[rightpointer]
        s[rightpointer] = temp
        leftpointer += 1
        rightpointer -= 1
    print(s)

s= ["h","e","l","l","o"]
reverseStringself(str(s))


