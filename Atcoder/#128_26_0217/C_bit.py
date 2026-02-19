n, m = map(int,input().split())
sk = []
for i in range(n):
    s = list(map(int,input().split()))
    sk.append(s)
p = list(map(int,input().split()))
for i in range(1 << n):
    cond = [0]*n
    cnt = 0
    for j in range(n):
        if 1 & (i >> j):
            cond[j] = 1
        if (j + 1) in sk[i]:
            print(j)
    print(cond)
