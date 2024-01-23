def romanToInt(s: str) -> int:
    symbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    val=0
    if s=="":
        return 0
    else:
        for x in range(len(s)-1):
            if symbols.get(s[x])<symbols.get(s[x+1]):
                val-=symbols.get(s[x])
            else:
                val+= symbols.get(s[x])
        return val+symbols.get(s[-1])


s = "IV"
#s="LVIII"

print(romanToInt(s))