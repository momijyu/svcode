import sys
s = set()
input = sys.stdin.readline
n, q = map(int,input().split())
for i in range(q):
    l,r = map(int,input().split())
    for i in range(l,r+1):
        s.add(i)
    print(n - len(s))