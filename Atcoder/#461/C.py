n, k, m = map(int, input().split())
vc = []
sel_col = set()
idx = set()
ls = 0
for i in range(n):
    ci, vi = map(int, input().split())
    vc.append((vi, ci))
vc.sort(reverse= True)
ans = 0
i = 0
while True:
    if m <= ls:
        break
    v, c = vc[i]
    if c not in sel_col:
        sel_col.add(c)
        ls += 1
        ans += v
        idx.add(i)
    i += 1
i = 1
#print(ans)
while True:
    if k <= ls:
        break
    v, c = vc[i]
    if i not in idx:
        ans += v
        ls += 1
    i += 1
print(ans)