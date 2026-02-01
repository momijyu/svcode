n = int(input())
l = []
for i in range(n):
    m = []
    for j in range(i + 1):
        if j == 0 or j == i:
            m.append(1)
        else:
            m.append(l[j]+l[j-1])
    for x in range(len(m)):
        print(m[x],end = " ")
    print()
    l = m