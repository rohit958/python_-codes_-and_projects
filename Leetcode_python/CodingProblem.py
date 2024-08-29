test_string = "Hello!, World! 123 2024 Welcome' to 2024 Hello!"
#remove every ! except last one
#remove every number except last 2024


res=test_string.replace("!","",(test_string.count("!")-1))
res=res.replace("2024","",(test_string.count("2024")-1))
res=res.replace("'","")

result=""
res=res.split()

for word in res:
    if word.isdigit() and word!='2024':
        continue
    result+=" "+word
print(result)













