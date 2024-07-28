
s="adfaa afa# fafe@!gsgs vava, by@e."
new=""
allowed=[',','.']
for x in s:
    if x.isalnum() or x==" " or x in allowed:
        new=new+x
print(new)
