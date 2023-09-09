def countGoodSubstrings(s: str):
    goodString=0
    for x in range(0,len(s)-2):
        window=s[x:x+3]
        if window[0]!= window[1] and window[0]!=window[2] and window[1]!=window[2]:
            goodString+=1
    return goodString


print(countGoodSubstrings('xyzzaz'))