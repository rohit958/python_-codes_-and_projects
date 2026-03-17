str1="BABA"
str2="AABB"

def calculate_freq(string):
  char_freq={}
  for char in string:
    if char in char_freq:
      char_freq[char]+=1
    else:
      char_freq[char]=1
  return char_freq    

print(calculate_freq(str1))
print(calculate_freq(str2))   