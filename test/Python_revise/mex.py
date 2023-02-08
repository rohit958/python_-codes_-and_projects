lis=[2,1,0,5]


lis.sort()
m=max(lis)

for i in range(len(lis)):
    for j in range(m):
        if j==lis[i]:
            pass
        if j not in lis:
            mex=j
            break

print(mex)