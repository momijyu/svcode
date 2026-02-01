n, m, k= map(int,input().split())
h = list(map(int,input().split()))
b = list(map(int,input().split()))
count = i = j = 0
h.sort()
b.sort()
while i <= n and j < m:
    if h[i] <= b[j]:
        i += 1
        j += 1
        count += 1
    else:
        j += 1
    if count >= k:
        break
if count < k:
    print("No")
else:
    print("Yes")