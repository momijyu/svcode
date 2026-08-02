n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0
for i in range(n-1):
    #print(111,a[i]+a[i+1]%m,b[i])
    if (a[i]+a[i+1])% m != b[i]:
        ans += 1
        a[i+1] += 1
print(min(ans, n-ans))