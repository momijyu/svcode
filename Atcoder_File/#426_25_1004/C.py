n, q = map(int,input().split())
p = []
for i in range(n):
  p.append((i+1, 1))
print(p)
for i in range(q):
  x, y = map(int,input().split())
  cnt = 0
  for j in range(n):
    if p[j][1] <= x:
      cnt += 1
      p[j] = (p[j][0], y)
print(cnt)
print(p)