n = int(input())
grid= []
maxnum = 0
maxidx = (0,0)
for i in range(n):
    a = str(input())
    grid.append(a)
    for j in range(n):
        if maxnum < int(a[j]):
            maxnum = int(a[j])
            maxidx = (i, j)
ans = 0
print(maxnum, maxidx)
for i in range()