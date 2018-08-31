import copy
t=int(input())
for tt in range(t):
  s=int(input())
  engines=[]
  for _ in range(s):
    engines.append(input())
  searches=[]
  q=int(input())
  for _ in range(q):
    searches.append(input())
  ans=0
  stack=[]
  while len(searches):
    a=searches[0]
    if a not in stack:
      stack.append(a)
    if len(stack)==s:
      stack=[]
      stack.append(a)
      ans+=1
    searches.pop(0)
  print("Case #"+str(tt+1)+": "+str(ans))
