n, m = map(int,input().split())
c = list(map(int,input().split()))
p = [0] * m
for i in range(n):
    a, b = map(int,input().split())
    p[a-1] += b
for i in range(m):
    if p[i] > c[i]:
        p[i] = c[i]
print(sum(p))