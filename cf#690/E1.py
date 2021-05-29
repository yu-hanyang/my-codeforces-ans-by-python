# for _ in range(int(input())):
#     n=int(input())
#     a=list(map(int,input().split()))
#     a.sort()
#     d={}
#     for i in range(n):
#         if a[i] in d:
#             d[a[i]]=i
#         else:
#             d[a[i]]=i
#     t=0
#     for i in range(0,n-2):
#         if a[i]+2 in d:
#             j=d[a[i]+2]
#             if j-i>1:
#                 t+=(j-i)*(j-i-1)//2
#         elif a[i]+1 in d:
#             j=d[a[i]+1]
#             if j - i > 1:
#                 t += (j - i) * (j - i - 1) // 2
#         elif a[i] in d:
#             j=d[a[i]]
#             if j - i > 1:
#                 t += (j - i) * (j - i - 1) // 2
#     print(t)
import sys
input=sys.stdin.readline
for _ in range(int(input())):
	n=int(input())
	a=sorted(list(map(int,input().split())))
	i,j,ans=0,2,0
	while j<n:
		if a[j]-a[i]<=2:
			ans+=((j-i-1)*(j-i))//2
			j+=1
		else:
			i+=1
		if j-i==1:j+=1
	print(ans)