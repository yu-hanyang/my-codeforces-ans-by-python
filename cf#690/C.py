from functools import reduce
for _ in range(int(input())):
    n=int(input())
    if n>45:
        print(-1)
    elif n<10:
        print(n)
    else:
        a=[]
        i=9
        while n>0:
            if n>=i:
                a.append(i)
                n-=i
                i-=1
            else:
                a.append(n)
                n=0
        a.sort()
        b=0
        for i in a:
            b=b*10+i
        print(b)