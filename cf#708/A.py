
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    c=list(set(a))
    for i in c:
        a.remove(i)
    print(*(c+a))