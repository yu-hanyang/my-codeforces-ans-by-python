for _ in range(int(input())):
    n=int(input())
    a=n//2020

    b=n%2020
    
    if b<=a:
        print('Yes')
    else:
        print('No')