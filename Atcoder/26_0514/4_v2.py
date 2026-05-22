s = str(input())
l = []
for i in s:
    if i == "a":l.append(0)
    if i == "t":l.append(1)
    if i == "c":l.append(2)
    if i == "o":l.append(3)
    if i == "d":l.append(4)
    if i == "e":l.append(5)
    if i == "r":l.append(6)
ans = 0
for i in range(len(l)):
    for j in range(i):
        if l[i] < l[j]:
            ans += 1
print(ans)