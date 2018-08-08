from collections import Counter
t=int(input())
for i in range(1,t+1):
    r,c=map(int,input().split())
    l=[]
    rr=[]
    s=[]
    for p in range(r):
        ll=list(input())
        if Counter(ll)['?']==c:
            l.append(ll)
            rr.append(p)
        elif '?' in ll and Counter(ll)['?']<c:
            for j in range(len(ll)):
                if ll[j] is not '?':
                    if (j-1)>=0 and ll[j-1]=='?':
                        k=j-1
                        while k>=0 and ll[k]=='?':
                            ll[k]=ll[j]
                            k-=1
                    if (j+1)<c and ll[j+1]=='?':
                        k=j+1
                        while k<c and ll[k]=='?':
                            ll[k]=ll[j]
                            k+=1                
            l.append(ll)
            s=ll
        else:
            l.append(ll)
            s=ll
        while len(rr) and len(s):
            l[rr[0]]=s
            rr.pop(0)
    print('Case #'+str(i)+':')
    for j in range(len(l)):
        s=''.join(l[j])
        print(s)
