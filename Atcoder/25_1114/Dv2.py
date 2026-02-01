n = int(input())
a = list(map(int,input().split()))
b = a[0]/a[1]
check = True
if n > 2:
    for i in range(n-1):
        if a[i]/a[i+1] != b:
            check = False
            break
if check:
    print("Yes")
else:
    print("No")