s = str(input())
num = ""
for i in range(-3, 0, 1):
    num += s[i]
if int(num) < 350 and num != "316" and num != "000":
    print("Yes")
else:
    print("No")