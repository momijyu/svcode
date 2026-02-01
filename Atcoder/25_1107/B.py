n, l, r = map(int,input().split())
a =list(range(1,n+1,1))
a[l-1:r] = reversed(a[l-1:r])
for i in range(len(a)):
    print(a[i], end=" ")