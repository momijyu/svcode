n= int(input())
a= list(map(int,input().split()))
b= list(map(int,input().split()))
a.sort()
a.reverse()
b.sort()
b.reverse()
c= 0
d= 0
count = 0
ans = -1
while((c <= n-1 or d <= n-2 )and count != 2):
    if d >= n - 1 or a[c] > b[d]:
        d -= 1
        ans = a[c]
        count += 1
    c += 1
    d += 1
if(count == 1):
    print(ans)
else:
    print(-1)