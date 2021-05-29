for _ in range(int(input())):
    n,d=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    if a[-1]<=d:
        print('YES')
    elif a[0]+a[1]<=d:
        print('YES')
    else:print('NO')