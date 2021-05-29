for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    if n<2*k+1:
        print('NO')
    elif k==0:
        print('YES')
    else:
        t=0
        for i in range(k):
            if s[i]!=s[n-i-1]:
                t=1
                break
        if t==1:
            print('NO')
        else:
            print('YES')