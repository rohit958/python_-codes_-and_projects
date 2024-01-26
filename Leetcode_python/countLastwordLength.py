sentence="hello world"

def lengthOfLastWord( s):
    s=s.strip()
    list=s.split(" ")
    return len(list[-1])

print(lengthOfLastWord(sentence))