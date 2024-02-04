def firstUniqChar( s: str) -> int:
    res = {}
    freq=0
    for x in s:
        if x not in res:
            res[x]=1
        else:
            res[x]+=1

    for x in range(len(s)):
        if res[s[x]]==1:
            return x

s = "aadadaad"
print(firstUniqChar(s))