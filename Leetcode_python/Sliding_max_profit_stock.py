pricing=[2,4,6,7,2,1,5,7,3,1]

l,r=0,1
maxprofit=0

while r< len(pricing)-1:
  if pricing[l]< pricing[r]: #we need sell only if selling point is greater than buying price
    profit=pricing[r]-pricing[l] #calculating profit
    maxprofit=max(maxprofit,profit)
  else:
    l=r
  r+=1
print(maxprofit)