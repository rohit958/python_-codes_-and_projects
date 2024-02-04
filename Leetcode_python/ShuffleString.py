def restoreString( s, indices):
    pos = {}
    res=""
    for x in range(len(indices)):
        pos[indices[x]] = s[x]

    for x in range(len(s)):
        res+=pos.get(x)
    return res

s=s = ("codeleet")
indices = [4,5,6,7,0,2,1,3]

print(restoreString(s,indices))
