n, m = map(int,input().split())
a = list(map(int,input().split()))
sum = 0
check = False
for i in range(len(a)):
    sum += a[i]
for i in range(n):
    if sum - a[i] == m:
        check = True
        break
if check:
    print("Yes")
else:
    print("No")