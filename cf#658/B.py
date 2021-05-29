for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.pop()
    if 1 not in a:
        print('First')
    else:
        a_1=0
        for i in a:
            if i==1:
                a_1+=1
            else:
                break
        if a_1%2==1:
            print('Second')
        else:
            print('First')
