
def decrypt( code, k) :
    res=[]
    l=len(code)
    if k>0:
        ele=sum(code[:k])
        for i in range(l):
            ele=ele-code[i]+code[(k+i)%l]
            res.append(ele)
    elif k<0:
        ele=sum(code[k:])
        for i in range(l):
            res.append(ele)
            ele=ele+code[i]-code[(k+i)%l]
    else:
        res=[0]*l

    return res