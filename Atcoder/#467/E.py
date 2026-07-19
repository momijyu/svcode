n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0
for i in range(n-1):
    #print(111,a[i]+a[i+1]%m,b[i])
    x = ((a[i]+a[i+1])%m)
    print(x)
    if x <= b[i]:
        ans += b[i]-x
        a[i+1] += b[i]-x
        print(2222,a)
    else:
        ans += m -x +b[i]
        a[i+1] += m -x +b[i]
        print(33333,a)

print(min(ans, n-ans))