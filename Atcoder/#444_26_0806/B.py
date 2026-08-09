n, k = map(int,input().split())
ans = 0
for i in range(n+1):
    s = list(str(i))
    sm = 0
    for j in s:
        sm += int(j)
    if sm == k :
        ans += 1
print(ans)