s = list(map(int,input().split()))
check = True
for i in range(len(s)-1):
    if s[i] >= s[i+1]:
        check = False
    if s[i] % 25 != 0:
        check = False
if max(s) >= 675 and min(s) <= 100:
    check = False
if check:
    print("Yes")
else:
     print("No")