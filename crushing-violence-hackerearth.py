from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    b=list(map(int,input().split()))
    g=list(map(int,input().split()))
    bbg=b+g
    x=max(bbg)
    beatb={}
    beatg={}
    for i in range(1,x+1):
        beatb[i]=0
        beatg[i]=0 
    for i in range(n):
        if g[b[i]-1]!=b[i]:
           beatb[g[b[i]-1]]+=1
    for i in range(n):
        if b[g[i]-1]!=g[i]:
            beatg[b[g[i]-1]]+=1
    beat=max([max(beatb.values()),max(beatg.values())])
    relbg={x+1:b[x] for x in range(0,n)}
    relgb={x+1:g[x] for x in range(0,n)}
    fightb={}
    fightg={}
    for key in relbg.keys():
        if relgb[relbg[key]]!=key:
            fightb[key]=relgb[relbg[key]]
    for key in relgb.keys():
        if relbg[relgb[key]]!=key:
            fightg[key]=relbg[relgb[key]]
    c=0
    for key in fightb.keys():
        try:
            if key==fightb[fightb[key]]:
                c+=1
        except:
            continue
    for key in fightg.keys():
        try:
            if key==fightg[fightg[key]]:
                c+=1
        except:
            continue
    print(beat,int(c/2))                
