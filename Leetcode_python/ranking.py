def arrayRankTransform(arr) :
    temp=sorted(set(arr))
    rank={}
    res=[]
    count=1
    for x in temp:
        rank[x]=count
        count+=1
    #while i < k:
    #       res.append(arr[k - x - 1])
    for x in arr:
        res.append(rank[x])
    return res
arr=[40,10,20,30]
print(arrayRankTransform(arr))
