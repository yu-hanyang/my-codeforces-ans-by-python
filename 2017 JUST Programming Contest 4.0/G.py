for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    z=''
    zz=a[0]
    f=''
    ff=a[-1]
    for i in range(1,n-1):
        if zz<=a[i]:
            z=z+'1'
            zz=a[i]
        else:
            z=z+'0'
        if ff>=a[-1-i]:
            f=f+'1'
            ff=a[-1-i]
        else:
            f=f+'0'

    if n>2:
        out=0
        an=int(f[::-1],2)&int(z,2)
        out=bin(an)[2:].count('1')
        print(out)
    else:print(0)

