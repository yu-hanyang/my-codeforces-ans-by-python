for _ in range(int(input())):
    n=int(input())
    a=input()
    b=input()
    kk=[0]
    a_b=bin(int(a,2)^int(b,2))[2:]
    if len(a_b)<n:
        a_b='0'*(n-len(a_b))+a_b
    k_1=0
    for i in range(n-1,-1,-1):
        if a_b[i]=='1':
            wz1=i
            k_1+=1



        elif k_1>0 and a_b[i]=='0':
            kk[0]+=3
            kk.append(wz1+k_1)
            kk.append(k_1)
            kk.append(wz1+k_1)
            k_1=0
        if i==0 and k_1>1:
            for j in range(k_1-1,-1,-1):
                if j==0:
                    kk[0]+=1
                    kk.append(1)
                else:
                    kk[0]+=3
                    kk.append(j+1)
                    kk.append(1)
                    kk.append(j+1)
        elif i==0 and k_1==1:
            kk[0]+=1
            kk.append(k_1)
    print(*kk)

