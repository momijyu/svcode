n = int(input())
a = list(map(int,input().split()))
c = True
if n > 2:
    for i in range(n-2):
        if a[i]*a[i+2] != a[i+1]*a[i+1]:
            c = False
            break
if c:
    print("Yes")
else:
    print("No")