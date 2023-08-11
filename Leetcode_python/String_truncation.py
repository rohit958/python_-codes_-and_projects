'''
Input: s = "Hello how are you Contestant", k = 4
Output: "Hello how are you"
Explanation:
The words in s are ["Hello", "how" "are", "you", "Contestant"].
The first 4 words are ["Hello", "how", "are", "you"].
Hence, you should return "Hello how are you".
'''

def truncateSentence( s, k):
    words=s.split()
    strng=words[0]
    loop_counter=1
    while loop_counter <k :
        strng=strng + " " + words[loop_counter]
        loop_counter+=1
    return strng


print(truncateSentence("What is the solution to this problem",4))