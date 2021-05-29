for _ in range(int(input())):
    n=int(input())
    a=input()
    if a[:1]=='2' and a[-3:]=='020':
        print('Yes')
    elif a[:2]=='20' and a[-2:]=='20':
        print('Yes')
    elif a[:3]=='202' and a[-1:]=='0':
        print('Yes')
    elif a[:4]=='2020':
        print('Yes')
    elif a[-4:]=='2020':
        print('Yes')
    else:
        print('No')