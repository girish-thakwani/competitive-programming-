t=int(input())
def bfs(s):
    q=[]
    q.append(s)
    visited[s]=True
    ans=[]
    while len(q):
        p=q[0]
        q.pop(0)
        ans.append(p)
        try:
            if d[p]:
                if not visited[d[p]]:
                    q.append(d[p])
                    visited[d[p]]=True
        except:
            break
    s=""
    for j in range(len(ans)-1):
        s=s+ans[j]+"-"+ans[j+1]+" "
    print("Case #"+str(i)+": "+s)

for i in range(1,t+1):
    n=int(input())
    d={}
    visited={}
    for j in range(n):
        a,b=input(),input()
        d[a]=b
        visited[b]=False
        visited[a]=False
    source=None
    for key,value in d.items():
        if key not in d.values():
            source=key
            break
    bfs(source)
            
