n = int(input())
s = str(input())
check = True
for i in range(n-1):
    if s[i] == "F":
        if s[i+1] != "M":
            check = False
    if s[i] == "M":
        if s[i+1] != "F":
            check = False
if check:
    print("Yes")
else:
    print("No")