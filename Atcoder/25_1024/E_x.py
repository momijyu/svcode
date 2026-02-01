n, m = map(int,input().split())
s = list(str(input()))
c = list(input().split())
l1 = []
l2 = []
count = []
for i in range(m):
    count.append(0)
print(c)
for i in range(m):
    for j in range(n):
        if c[j] == str(i+1):
            l1.append(s[j])
            #print(l1)
    l2.append(l1)
    l1 = []
for i in range(n):
    print(l2[[c[i]][int(count[c[i]])]])