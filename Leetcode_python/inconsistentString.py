#when unique elements are needed to be searhced use set

def countConsistentStrings( allowed, words):
    test_char= set(allowed)
    cnt=0
    for word in words:
        isconsistent=True
        for char in word:
            if char not in test_char:
                isconsistent=False
                break
        if isconsistent is True:
            cnt+=1
    return cnt
allowed = "cad"

words = ["cc","acd","b","ba","bac","bad","ac","d"]

print(countConsistentStrings(allowed,words))

