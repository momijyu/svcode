n, m, t = map(int,input().split())
a = list(map(int, input().split()))
l = []
n -= 1
chack = True
for i in range(m):
    p = list(map(int,input().split()))
    l.append(p)

i = 0
while i <= n-1:
    if t - a[i] >= 0:
        t -= a[i]
        i += 1
    else:
        print("No")
        chack = False
        break
    for x, y in l:
        if i+1 == x:
            t += y
if chack:
    print("Yes")