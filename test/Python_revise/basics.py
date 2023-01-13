a,b=2,3

def swap(a,b):
    temp=a
    a=b
    b=temp

if __name__=='__main__':
    print("before swapping:",a,b)
    swap(a,b)
    print("after swapping:",a,b)

