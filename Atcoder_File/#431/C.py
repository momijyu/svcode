n, m, k= map(int,input().split())
h = list(map(int,input().split()))
b = list(map(int,input().split()))
count = 0
for i in range(n):
    if max(h) <= max(b):
        h[h.index(max(h))] = 0
        b[b.index(max(b))] = 0
        count += 1
    else:
        h[h.index(max(h))] = 0
    if count >= k:
        break
if count < k:
    print("No")
else:
    print("Yes")
