n, m = map(int,input().split())
l = []
se = set()
for i in range(n):
    s = list(map(str,input().split()))
    l.append(s)
print(l)
for i in range(0, n-m+1):
    s = ""
    for j in range(0,n-m+1):
        print (l[i][j])
        for x in range(m):
            for y in range(m):
                s += 
print(s)