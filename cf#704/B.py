for _ in range(int(input())):
    n=int(input())
    p=list(map(int,input().split()))
    out=[]
    pp=sorted(p,reverse=True)
    t=0
    maxt=pp[t]
    bt=len(p)
    for i in range(len(p)-1,-1,-1):
        if i==0:
            out.extend(p[i:bt])

        elif p[i]==maxt:
            out.extend(p[i:bt])
            while pp[t] not in p[:i]:
                t+=1
            maxt=pp[t]
            bt=i

    print(*out)

