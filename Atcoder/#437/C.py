t = int(input())
for i in range(t):
    w = []
    p = []
    sum = []
    n = int(input())
    powers = 0
    for i in range(n):
        l,m = list(map(int,input().split()))
        w.append(l)
        p.append(m)
        powers += m
        sum.append(l+m)
    sum.sort()
    cnt = 0
    sumsum = 0
    for i in sum:
        if sumsum + i <= powers:
            sumsum += i
            cnt += 1
        else:
            break
    print(cnt)