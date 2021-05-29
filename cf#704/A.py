for _ in range(int(input())):
    p,a,b,c=map(int,input().split())
    if p==0:
        print(0)
    else:
        if a<p:
            a1=(p-a)//a
            if (p-a)%a==0:
                a=a*(a1+1)
            else:
                a=a*(a1+2)
        if b < p:
            b1 = (p - b) // b
            if (p - b) % b == 0:
                b = b * (b1 + 1)
            else:
                b = b * (b1 + 2)
        if c < p:
            c1 = (p - c) // c
            if (p - c) % c == 0:
                c = c * (c1 + 1)
            else:
                c = c * (c1 + 2)
        print(min(a-p,b-p,c-p))


