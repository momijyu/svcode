n, m = map(int,input().split())
s = set()
dab = []
col = [0] *(n+1)
for i in range(n):
    ai, di, bi = map(int,input().split())
    if di != 1:
        s.add(ai)
        col[ai] += 1
        dab.append((di, ai, bi))
    else:
        s.add(bi)
        col[bi] += 1
#print(dab, s)
#print(col)
dab.sort()
cols = len(s)
print(cols)
#print(dab)
i = 0
q = len(dab)
for j in range(2, m + 1):
    while i < q and dab[i][0] == j:
        d, a, b = dab[i]
        col[a] -= 1
        if col[a] == 0:
            cols -= 1
        if col[b] == 0:
            cols += 1
        col[b] += 1
        i += 1
    print(cols)
    print(col)