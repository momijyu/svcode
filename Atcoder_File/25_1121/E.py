n, m = map(int,input().split())
u = []
v = []
c = [""]*n
count = 0
print(c)
for i in range(m):
    a, b = map(int,input().split())
    u.append(a)
    v.append(b)
print(c[0])
c[u[0]-1] = True
c[v[0]-1] = False
for i in range(m):
    if (c[u[i]] == True and c[v[u[i]]] == True)or(c[u[i]] == False and c[v[i]] == False):
        count += 1
    else:
        if c[u[i]] == True:
            c[v[i]] = False
        elif c[u[i]] == False:
            c[v[i]] == True
        elif c[v[i]] == True:
            c[u[i]] = False
        elif c[v[i]] == False:
            c[u[i]] = True
        else:
            c[u[i]] = True
            c[v[i]] = False
print(count)