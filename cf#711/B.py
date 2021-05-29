for _ in range(int(input())):
    n, m = map(int, input().split())
    s=list(map(int,input().split()))
    #s = [int(i) for i in input().split()]
    d = dict()
    s.sort(reverse=True)
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    m1 = m
    ans = 0
    while (n > 0):
        for j in d:
            while d[j] > 0 and j <= m1:
                m1 = m1 - j
                d[j] -= 1
                # print(m1,j)
                n -= 1
        m1 = m
        ans += 1
        # print(n)

    print(ans)