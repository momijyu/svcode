H, S = map(int,input().split())
l = []
t = "sunke"
for i in range(H):
    l.append(input())
print(l)
for i in range(H):
    if t[0] in l[i]:
        p = l[i].index(t[0])
        if t in l[i]:
            for j in range(p,S):
                print(i, j)