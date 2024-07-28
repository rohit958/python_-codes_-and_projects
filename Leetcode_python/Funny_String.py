def funnyString(s):
    list1 = []
    absdiff = []
    absrev = []
    list2=[]
    for char in s:
        list1.append(ord(char))
    list2=list1[::-1]

    for x in range(len(list1) - 1):
        j = abs(list1[x] - list1[x + 1])
        k = abs(list2[x] - list2[x + 1])
        absdiff.append(j)
        absrev.append(k)

    if absdiff == absrev:

        return ("Funny")
    else:
        return ("Not Funny")


print(funnyString("bcxz"))