def longestPalindrome( s: str) -> int:
    dic = {}
    total = 0
    flg = 0
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic:
        if dic[i] % 2 == 0:
            total += dic[i]
        else:
            flg = 1
            total += dic[i] - 1
    if flg == 1:
        return total + 1
    return total

print(longestPalindrome("abccccdd"))