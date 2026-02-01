n, m = map(int, input().split())
from collections import Counter
x = []
y = []
z = []
for i in range(m):
    lx, ly = map(int,input().split())
    x.append(lx)
    y.append(ly)
    z.append(lx)
    z.append(ly)
print(x)
print(y)
print(z)
cx = Counter(x)
cy = Counter(y)
cz = Counter(z)
print(cz)