s = str(input())
n = ""
for i in range(3,0,-1):
    n += s[-i]

if int(n) < 350 and int(n) != 316 and int(n) != 0:
    print("Yes")
else:
    print("No")