for _ in range(int(input())):
    m=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    n=-1
    for i,j in enumerate(a):
        if j*3<b[i]:
            n=i+1
            break
    print(n)