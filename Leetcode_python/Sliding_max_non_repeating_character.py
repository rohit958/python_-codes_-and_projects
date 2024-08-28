st="abcabcbb"

charset=set()
l=0
res=0


for r in range(len(st)):
  while st[r] in charset:
    charset.remove(st[r])
    l+=1
  charset.add(st[r])
  res=max(res,r-l+1)
print(res)


