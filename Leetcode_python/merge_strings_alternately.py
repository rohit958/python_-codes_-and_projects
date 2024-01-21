word1 = "abc"
word2 = "pqr"


def mergeAlternately( word1: str, word2: str):
    res = ""
    len1 = len(word1)
    len2 = len(word2)
    i, j = 0, 0
    while i < len1 or j < len2:
        if i < len1 and j < len2:
            res += word1[i] + word2[j]
            i += 1
            j += 1
        elif i >= len1:
            res += word2[j]
            j += 1
        elif j >= len2:
            res += word1[i]
            i += 1
    return res


print(mergeAlternately(word1, word2))
