t=int(input())
for k in range(1,t+1):
    n=[int(x) for x in str(input())]
    first=1
    for i in range(1,len(n)):
        if n[i]<n[i-1]:
            if n[i]==0 and n[i-1]==1:
                for j in range(len(n)-1,0,-1):
                    if j>i:
                        n[j]=9
                    elif n[j]>1:
                        n[j]-=1
                        break
                    else:
                        n[j]=9
                        first=0
            else:
                n[i-1]-=1
                for j in range(i,len(n)):
                    n[j]=9
    if first==0:
        n.pop(0)
    num=''.join(str(i) for i in n)
    print("Case #"+str(k)+": "+num)
