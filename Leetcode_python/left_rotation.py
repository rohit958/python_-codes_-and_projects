#left rotation

list=[1,2,3,4,5]

print("before rotation",list)

# left rotation for n using list comprehension
n=3
rotate=list[n:]+list[:n]
print("after rotation for {0} times:".format(n),rotate)