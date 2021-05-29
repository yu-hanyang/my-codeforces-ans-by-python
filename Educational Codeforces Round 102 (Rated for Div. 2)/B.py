import math
for _ in range(int(input())):
    s=input()
    t=input()
    l_s=len(s)
    l_t=len(t)
    s_s=''
    s_t=''
    for i in s:
        s_s=s_s+i
        if l_s%len(s_s)==0:
            if s_s*(l_s//len(s_s))==s:
                break
    for i in t:
        s_t = s_t + i
        if l_s % len(s_t) == 0:
            if s_t * (l_t // len(s_t))==t:
                break
    if s_s!=s_t:
        print(-1)
    else:
        gc=math.gcd((l_t//len(s_t)),(l_s//len(s_s)))
        lc=((l_s//len(s_s))*(l_t//len(s_t)))//gc

        print(s_s*lc)



