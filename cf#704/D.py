a,b,k=map(int,input().split())
if a+b-1<k:
    print('No')
else:
    if a+b-1==k:
        print('1'*b+'0'*a)a=
        print('0'*a+'1'*b)
