n = int(input())
s = str(input())
check = False
if "ab" in s or "ba" in s:
    check= True
if check:
    print("Yes")
else:
    print("No")
