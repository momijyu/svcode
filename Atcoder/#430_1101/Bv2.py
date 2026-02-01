def colch(s,a,b):
    if s[a][b] == ".":
        return "0"
    else:
        return "1"

n, m = map(int,input().split())
s = [input() for _ in range(n)]
p = set()
count = 0
for i in range(n-m+1):
    for j in range(n-m+1):
        l = []
        for k in range(m):
            r = s[i+k][j:j + m]
            l.append(r)
        p.add(l)
print(len(p))