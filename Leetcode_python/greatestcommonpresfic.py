def longestCommonPrefix( strs):
    commonprefix = ""
    minlength = len(strs[0])
    minwordindex=0
    for x in range(1,len(strs)):
        if len(strs[x])< minlength:
            minlength = len(strs[x])
            minwordindex=x
    for


strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))