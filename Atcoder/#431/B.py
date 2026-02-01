x = int(input())
n = int(input())
w = list(map(int,input().split()))
q = int(input())
s = set()
for i in range(q):
    p = int(input())
    if p not in s:
        s.add(p)
        x += w[p-1]
        print(x)
    else:
        s.remove(p)
        x -= w[p-1]
        print(x)