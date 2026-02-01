N, Q = map(int,input().split())
j = 0
n = 0
ver = []
comp = []
count = 0
for i in range(Q):
    ver += map(int,input().split())
for i in range(N):
    comp.append(1)
print(ver)
print(comp)
for i in range(Q):
    while j <= ver[n]-1:
        comp[ver[n]-1] += comp[j]
        count += comp[j]
        comp[j] = 0
        j += 1
    print(count)
    count = 0
    j = ver[n-1]
    n += 2
print(comp)