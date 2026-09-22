n = int(input())
s = []
check = False
for i in range(n):
    b = str(input())
    s.append(b) 
for i in range(n):
    for j in range(n):
        m = s[i] + s[j]
        w = str(m)[::-1]
        if m == w and i != j:
            check = True
if check:
    print("Yes")
else:
    print("No")