n, k, x= map(int,input().split())
a= list(map(int,input().split()))
a.sort()
ans = n-k
sum= 0
i= -(ans+1)
while i >= -n and sum < x:
    sum += a[i]
    i -= 1
    ans += 1
if sum < x:
    print(-1)
else:
    print(ans)