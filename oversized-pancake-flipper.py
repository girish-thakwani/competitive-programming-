t=int(input())
for q in range(t):
    s,k = input().split();k=int(k)
    s1=[]
    for i in s:
        if i=='-':
            s1.append(0)
        else:s1.append(1)
    y=0
    for i in range(len(s)-k+1):
        if s1[i]==0:
            for j in range(i,i+k):
                s1[j]=not s1[j]
            y+=1
    if all(s1):
        print("Case #"+str(q+1)+": "+str(y))
    else:
        print("Case #"+str(q+1)+": IMPOSSIBLE")
