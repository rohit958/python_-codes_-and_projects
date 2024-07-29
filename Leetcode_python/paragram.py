s='We promptly judged antique ivory buckles for the next prize'
l="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s=s.replace(" ","").lower()
print(s)
flag=0
for char in l:
    if char.lower() not in s:
        print("not pangram" )
        break
print("pangram")