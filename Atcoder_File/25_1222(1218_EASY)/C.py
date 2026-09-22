n, q = map(int,input().split())
l = []
for i in range(n):
    b = list(map(int,input().split()))
    l.append(b)
for i in range(q):
    s,t = map(int,input().split())
    print(l[s][t])