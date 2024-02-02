def longestNiceSubstring(s: str):
   x=0
   lim=len(s)
   res=""
   pos_y=False
   done=[]
   while x< lim:
       if x in done or s[x].upper() in res or s[x].lower() in res:
           x += 1
           continue
       else:
           if s[x].isupper() :
               for y in range(x+1,lim):
                   if s[y]==s[x].lower():
                       res+=s[x]+s[y]
                       done.append(y)
           else :
               for y in range(x+1,lim):
                   if s[y]==s[x].upper():
                       res+=s[x]+s[y]
                       done.append(y)
       x+=1
   return res

s = "Bxyzbb"
print(longestNiceSubstring(s))
