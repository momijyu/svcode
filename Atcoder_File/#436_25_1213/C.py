n, m = map(int,input().split())
count = 0
s = set()
for i in range(m):
    r, c = map(int,input().split())
    t = (r,c)
    if t not in s:
        count += 1
        s.add(t)
        t = (r+1, c)
        s.add(t)
        t = (r, c+1)
        s.add(t)
        t = (r+1, c+1)
        s.add(t)
print(count)