n = int(input())
lr= []
for i in range(n):
    a, b = map(int,input().split())
    lr.append((a,b))
lr.sort()
d = []
l, r = lr[0]
for i in range(1,n):
    n_l, n_r = lr[i]
    if n_l <= r:
        r = max(r, n_r)
    else:
        d.append((l,r))
        l, r = n_l, n_r
d.append((l,r))
for i,j in d:
    print(i,j)