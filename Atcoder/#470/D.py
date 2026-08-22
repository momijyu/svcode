n, q = map(int,input().split())
p = list(map(int,input().split()))
p = [0]+ p
z = [0]*(n+1)
#iとvを入れ替えた値
for i in range(1,n+1):
    z[p[i]] = i
#print(z)
check = True
for i in range(q):
    a = list(map(int,input().split()))
    if a[0] == 1:
        x,y = a[1],a[2]
        if check:
            z[p[x]], z[p[y]] = y, x
            p[x], p[y] = p[y], p[x]
        else:
            p[z[x]], p[z[y]] = y, x
            z[x], z[y] = z[y], z[x]
    else:
        check = not check
if check:
    print(*(p[1:]))
else:
    print(*(z[1:]))
    