t, x = map(int,input().split())
a = list(map(int,input().split()))
max_n = a[0]
print(0,a[0])
for i in range(t+1):
    if abs(a[i] - max_n) >= x:
        max_n = a[i]
        print(i,max_n)