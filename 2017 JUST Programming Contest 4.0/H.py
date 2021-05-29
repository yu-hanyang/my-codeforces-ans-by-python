for _ in range(int(input())):
    n,m=map(int,input().split())
    a0=0
    a1=0
    for i in range(n):
        a=input()
        if i==0 or i==n-1:
            a0+=a.count('0')
        else:
            a1+=a[1:m-1].count('1')
            if a[0]=='0':
                a0+=1
            if a[-1]=='0':
                a0+=1
    if a0<=a1:
        print(a0)
    else:print(-1)
