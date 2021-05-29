for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    sum_a=sum(a)
    for i in range(n,0,-1):
        if sum_a%i==0:
            t=0
            av=sum_a//i
            b=a
            for j in range(1,n):
                if b[j-1]+b[j]<=av:
                    b[j]=b[j]+b[j-1]
                    t+=1
            if t+1==i:
                print(n-t)
                break

