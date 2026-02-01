x, y, z= map(int,input().split())
check = True
d = x - y*z
if d % 2 == 0:
    check = False
if x < y*z:
    check = True
if check:
    print("No")
else:
    print("Yes")