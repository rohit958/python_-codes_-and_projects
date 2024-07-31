s="abcjafefjkajcefeahcafat"

# count number of characters in string

freq={}

for char in s:
    if char not in freq:
        freq[char]=1
    else:
        freq[char]+=1

for key, value in freq.items():
    print(key,":",value)