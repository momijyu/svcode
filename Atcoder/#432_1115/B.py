x = int(input())
x = str(x)
m = []
for i in range(len(x)):
    m.append(x[i])
m.sort()
i = 0
check = False
while i <= len(x)-1: 
    if m[i] != "0":
        j = m[i]
        m[i] = m[0]
        m[0] = j
        break
    i += 1
for i in m:
    print(i,end="")
