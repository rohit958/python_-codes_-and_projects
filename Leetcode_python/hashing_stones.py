
def numJewelsInStones(jewels, stones):
    cnt = 0
    for x in jewels:
        for k in stones:
            if x==k:
                cnt += 1
    return cnt

print(numJewelsInStones("aA","aAAbbbb"))