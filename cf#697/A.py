s=int(input())
for j in range(s):
    flag = 0
    n=int(input())
    if n%2==1:
        flag=1
    else:
        while n%2==0:
            n=n//2
        if n!=1:
            flag=1
    if flag==1:
        print("YES")
    else:
        print("NO")
