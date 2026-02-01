n = int(input())
a = list(map(int,input().split()))
c = a[1] / a[0]
check = False
for i in range(1,n-1):
    if a[i]*c != a[i+1]:
        check = True
        break
if check:
    print("No")
else:
    print("Yes")