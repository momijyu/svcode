n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
b = [0]*m
c = [0]*m
for i in range(n):
    b[a[i][0]-1] += 1
    c[a[i][1]-1] += 1
for i in range(m):
    print(c[i]-b[i])