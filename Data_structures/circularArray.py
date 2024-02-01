#we use modulus(%) operator for finding index in circular queue

def prints(a, n, ind):
    i = ind

    # print from ind-th index to (n+i)th index.
    while i < n + ind:
        print(a[(i % n)], end=" ")
        i = i + 1


# Driver Code
a = ['A', 'B', 'C', 'D', 'E', 'F']
n = len(a)
prints(a, n, 3)






code = [5,7,1,4]
k = 3