# n,m=map(int,input().split())
# s=input()
# t=input()
# for
s='abbbc'
t='abc'

r=i=j=-1
a=[]
for x in t[:-2]:
    i=s.find(x,i+1)
    print(i)
    a+=i,
    print(a)
for x in t[-2:0:-1]:
    j=s.rfind(x,0,j)
    r=max(r,j-a.pop())
    print(j)
    print(r)
