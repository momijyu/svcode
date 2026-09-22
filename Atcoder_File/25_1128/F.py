n = int(input())
point = []
a = bin(n)
a = str(a)
for i in range(-1, -len(a), -1):
    if(a[i]=="0"):
        point.append(i)

for i in range(n):
    for j in range(len(point)):
        if i[point[j]]