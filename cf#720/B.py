import math
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=[]

    cnt=0
    for i in range(n-1):
        if math.gcd(a[i],a[i+1])!=1:
            cnt+=1
            if a[i]>a[i+1]:
                ans.append([i,i+1,a[i+1]+1,a[i+1]])
            else:
                ans.append([i,i+1,a[i],a[i]+1]

