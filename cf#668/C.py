for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    n_0=k//2
    n_1=k//2
    ls=[]
    t_1=0
    t_0=0
    for i in range(n):
        if i<k:
            if s[i]=='1':
                n_1-=1
            elif s[i]=='0':
                n_0-=1
            ls+=s[i],
        else:
            if i==k:
                t_0=int(n_0)
                t_1=int(n_1)
            # if n_0==0 or n_1==0:
            #     t_0=int(n_0)
            #     t_1=int(n_1)

                n_1=0
                n_0=0





            temp=ls.pop(0)
            if temp==s[i]:
                ls.append(s[i])
            else:
                if temp=='1' and s[i]=='?':
                    # t_1+=1
                    # n_1+=1
                    ls.append('1')
                elif temp=='0' and s[i]=='?':
                    # t_0+=1
                    # n_0+=1
                    ls.append('0')
                elif temp=='1' and s[i]=='0':
                    n_0-=1
                    n_1+=1
                    ls.append(s[i])
                elif temp=='0' and s[i]=='1':
                    n_1-=1
                    n_0+=1
                    ls.append(s[i])
                elif temp=='?' and s[i]=='1':
                    t_1-=1

                    ls.append(s[i])

                elif temp=='?' and s[i]=='0':
                    t_0-=1

                    ls.append(s[i])

        if (n_0<0 or n_1<0 or t_1<0 or t_0<0) :
            print('NO')
            break
    else:print('YES')