n, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
check = True
maxn = max(a)
for i in range(n):
    if a[i] == maxn:
        if(i+1) in b:
            check = False
if check:
    print("No")
else:
    print("Yes")
