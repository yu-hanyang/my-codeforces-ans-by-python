for _ in range(int(input())):
    n=int(input())
    a=input()
    b=input()
    kk=[0]
    for i in range(n-1,-1,-1):
        if a[i]!=b[i]:
            kk[0]+=3
            kk.append(i+1)
            kk.append(1)
            kk.append(i+1)
    print(*kk)
