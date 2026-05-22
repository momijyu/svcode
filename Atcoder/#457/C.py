n, k = map(int,input().split())
l = []
for i in range(n):
    le = list(map(int,input().split()))
    l.append(le)
c = list(map(int,input().split()))
tol = 0
tol_d = 0
for i in range(n):
    la = l[i][0]
    tol = c[i] * la
    if tol + tol_d >= k:
        s = k - tol_d
        print(l[i][(s-1) % la + 1])
        exit()
    tol_d += tol