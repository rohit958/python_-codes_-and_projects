
#solving first occurance in Strin problem
# Using sliding problem


def strStr( haystack: str, needle: str) -> int:

    start =0
    end = len(needle)
    if needle=="":
        return 0
    while end <= len(haystack):
        #print(haystack[start:end])
        if haystack[start:end] == needle:
            return start
        else:
            start = start+1
            end = end+1
    return -1

haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack,needle))