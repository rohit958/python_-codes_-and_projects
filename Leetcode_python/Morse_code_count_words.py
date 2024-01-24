#morse code

codes=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

morse_code={}
char=ord('a')
for x in codes:# loop to create dictionary
    morse_code[chr(char)]=x
    char+=1

def uniqueMorseRepresentations( words) -> int:
    res=set()

    for word in words:
        morse = ""
        for y in word:
            morse+=str(morse_code.get(y))
        if morse not in res:
            res.add(morse)

    return len(res)

words = ["gin","zen","gig","msg"]
print(uniqueMorseRepresentations(words))
