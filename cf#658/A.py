for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()
    if n>m:
        for i in b:
            if i in a:
                print('Yes')
                print(1,i)
                break
        else:
            print('No')
    else:
        for i in a:
            if i in b:
                print('Yes')
                print(1,i)
                break
        else:
            print('No')

