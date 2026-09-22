n = int(input())
a = list(map(int,input().split()))
a.sort()
a.reverse()
check = True
for i in range(n):
    if a[0] != a[i] and check:
        check = False
        print(a[i])
        exit
if check:
    print(a[i])