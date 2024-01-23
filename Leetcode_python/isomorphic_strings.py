# isomorphic- if strings are able to map to other string
# we compare using hashmap technique

def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    else:
        hashmap={}
        for x in range(len(s)):
            if s[x] not in hashmap:
                hashmap[s[x]]=t[x]
            if hashmap [s[x]]!=t[x]:
                return False
        return True
s="add"
t="egg"
print(isIsomorphic(s,t))





