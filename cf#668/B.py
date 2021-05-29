for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))

    cnt=0
    for i in a:
        if i>0:
            cnt+=i

        else:
            cnt+=i
            if cnt<0:
                cnt=0
    print(cnt)