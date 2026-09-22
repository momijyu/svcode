n, m = map(int,input().split())
s = set()
dab = []
for i in range(n):
    ai, di, bi = map(int,input().split())
    if di != 1:
        s.add(ai)
        dab.append((di, ai, bi))
    else:
        s.add(bi)
#print(dab, s)
ls= len(s)
dab.sort()
print(ls)
idx = 0
