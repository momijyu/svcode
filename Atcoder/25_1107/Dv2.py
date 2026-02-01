q = int(input())
l = []
m = []
for i in range(q):
    a = list(map(int,input().split()))
    m.append(a)
for i in range(q):
    if m[i][0]== 1:
        l.append(m[i][1])
    elif m[i][0] == 2:
        print(l[len(l)-m[i][1]])