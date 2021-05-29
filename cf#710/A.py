for _ in range(int(input())):
    n,m,x=map(int,input().split())
    n_z=x//n
    n_y=x%n
    if n_y==0:
        n_y=n
    else:n_z+=1

    print(m*(n_y-1)+n_z)