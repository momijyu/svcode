n, x, y = map(int,input().split())
a = list(map(int,input().split()))
a2 = []
d = y - x
minn = min(a)
maxn = max(a)
count = 0
for i in range(n):
    a2.append((a[i]-minn)*y)
    count += a[i]
    count -= a2[i]/d
if count != int(count) or (minn * y < maxn * x):
    print("-1")
else:
    print(int(count))